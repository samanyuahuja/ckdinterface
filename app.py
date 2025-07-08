from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import numpy as np
import shap 
import lime.lime_tabular
import matplotlib.pyplot as plt
import joblib
import os
import uuid
from sklearn.inspection import PartialDependenceDisplay

app = Flask(__name__)
app.secret_key = 'nephrosense_secret'

os.makedirs("static/plots", exist_ok=True)
@app.route('/')
def home():
    return render_template("index.html")  # ✅ this loads your index.html homepage  # 'index' points to /diagnosis
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@app.route('/diet')
def diet():
    return render_template("diet.html")

@app.route('/language')
def language():
    return render_template("language.html")


    # your form logic here
# Load model + scaler + train data
def load_resources(model_choice="rf"):
    if model_choice == "rf":
        model = joblib.load("models/rf_model_final.pkl")
    elif model_choice == "logistic":
        model = joblib.load("models/logistic_model_final.pkl")
    else:
        raise ValueError("Unknown model choice")
    
    scaler = joblib.load("models/scaler_final.pkl")
    try:
        X_train_res = joblib.load("models/X_train_res_scaled_final.pkl")
    except:
        X_train_res = None
    return model, scaler, X_train_res

model, scaler, X_train_res = load_resources("rf")

final_features = [
    'age', 'bp', 'al', 'su', 'rbc', 'pc', 'bgr', 'bu', 'sc',
    'sod', 'pot', 'hemo', 'wbcc', 'htn', 'dm', 'appet', 'pe',
    'ane', 'bun_sc_ratio', 'high_creatinine', 'hemo_bu'
]

def preprocess_input(df):
    mapper = {"normal": 0, "abnormal": 1, "present": 1, "notpresent": 0,
              "yes": 1, "no": 0, "good": 0, "poor": 1}
    categorical_cols = ['rbc', 'pc', 'ba', 'htn', 'dm', 'appet', 'pe', 'ane']

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].map(mapper).fillna(0)

    numeric_cols = ['age', 'bp', 'al', 'su', 'bgr', 'bu', 'sc',
                    'sod', 'pot', 'hemo', 'wbcc', 'rbcc']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    df["bun_sc_ratio"] = np.where(df["sc"] == 0, 0, df["bu"] / df["sc"])
    df["high_creatinine"] = (df["sc"] > 1.2).astype(int)
    df["hemo_bu"] = df["hemo"] * df["bu"]

    for col in final_features:
        if col not in df.columns:
            df[col] = 0

    return df[final_features]

@app.route('/diagnosis', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uid = str(uuid.uuid4())
        temp_input_path = f"static/temp_input_{uid}.csv"

        if 'csv_file' in request.files:
            file = request.files['csv_file']
            if file and file.filename != '':
                df = pd.read_csv(file)
                X_input_df = preprocess_input(df)
                X_input_df.to_csv(temp_input_path, index=False)
                return redirect(url_for('result', file=temp_input_path))

        # Form data
        form_data = {feature: request.form.get(feature) for feature in final_features}
        df = pd.DataFrame([form_data])
        X_input_df = preprocess_input(df)
        X_input_df.to_csv(temp_input_path, index=False)
        return redirect(url_for('result', file=temp_input_path))
    
    return render_template('diagnosis.html')

@app.route('/result')
def result():
    temp_file = request.args.get('file')
    if not temp_file or not os.path.exists(temp_file):
        flash("Input data missing or expired. Please re-submit.")
        return redirect(url_for('index'))

    X_input_df = pd.read_csv(temp_file)

    for col in scaler.feature_names_in_:
        if col not in X_input_df.columns:
            X_input_df[col] = 0
    X_input_df = X_input_df[scaler.feature_names_in_]

    X_scaled = scaler.transform(X_input_df)

    proba = model.predict_proba(X_scaled)[:,1]
    prediction = model.predict(X_scaled)
    no_ckd_proba = 1 - proba[0]

    # SHAP plot
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_scaled)

    plt.figure()
    shap.summary_plot(shap_values, X_scaled, feature_names=X_input_df.columns, show=False)
    shap_plot_path = f"static/plots/shap_summary_{uuid.uuid4()}.png"
    plt.savefig(shap_plot_path)
    plt.close()

    # PDP plot
    fig, axs = plt.subplots((len(final_features)+2)//3, 3, figsize=(15, 5 * ((len(final_features)+2)//3)))
    axs = axs.flatten()
    for i, feature in enumerate(final_features):
        PartialDependenceDisplay.from_estimator(model, X_train_res, [feature], ax=axs[i], feature_names=final_features)
    for j in range(i+1, len(axs)):
        fig.delaxes(axs[j])
    pdp_plot_path = f"static/plots/pdp_{uuid.uuid4()}.png"
    plt.savefig(pdp_plot_path)
    plt.close()

    # LIME plot generation
    lime_explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=np.array(X_train_res),
        feature_names=final_features,
        class_names=["No CKD", "CKD"],
        mode="classification",
        discretize_continuous=True
    )
    
    lime_exp = lime_explainer.explain_instance(
        data_row=X_scaled[0],
        predict_fn=model.predict_proba
    )
    
    lime_plot_path = f"static/plots/lime_{uuid.uuid4()}.png"
    lime_exp.as_pyplot_figure()
    plt.tight_layout()
    plt.savefig(lime_plot_path)
    plt.close()
    return render_template("result.html",
                           prediction=prediction[0],
                           proba=round(proba[0],3),
                           no_ckd_proba=round(no_ckd_proba,3),
                           shap_plot=shap_plot_path,
                           pdp_plot=pdp_plot_path
                           lime_plot=lime_plot_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
