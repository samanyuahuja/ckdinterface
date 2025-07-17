from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import make_response
from flask import request
import pandas as pd
import numpy as np
import shap  
import lime.lime_tabular
import matplotlib.pyplot as plt  
import joblib
import os
import uuid
from sklearn.inspection import PartialDependenceDisplay
from flask import make_response
from xhtml2pdf import pisa
from io import BytesIO



app = Flask(__name__)
app.secret_key = 'nephrosense_secret'

os.makedirs("static/plots", exist_ok=True)
@app.route('/')
def home():
    return render_template("index.html")  # ✅ this loads your index.html homepage  # 'index' points to /diagnosis
@app.route('/about')
def about():
    return render_template("about.html")
# Make sure to set your API key securely

@app.route("/chatbot")
def chatbot_page():
    return render_template("chatbot.html")

@app.route("/get_response", methods=["POST"])
def get_chatbot_response():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    msg = user_message.lower()

    if not msg:
        return jsonify({"reply": "Please enter a message."})

    # ---------------- RULE-BASED LOGIC ----------------
    if "what is ckd" in msg or "chronic kidney disease" in msg:
        reply = "Chronic Kidney Disease (CKD) is a condition where your kidneys lose function over time. It's usually caused by diabetes or high blood pressure."

    elif "symptoms" in msg:
        reply = "Common CKD symptoms include fatigue, swelling in legs, nausea, high blood pressure, and frequent urination."

    elif "treatment" in msg:
        reply = "CKD treatment depends on the stage. It usually includes managing blood pressure, blood sugar, and avoiding further kidney damage. In severe cases, dialysis or transplant may be needed."

    elif "diet" in msg:
        reply = "A CKD diet includes low-sodium, low-protein foods, avoiding processed items, and drinking enough water. Consult a nephrologist for a custom plan."

    elif "is ckd curable" in msg:
        reply = "CKD isn't curable but it can be managed effectively with medications, lifestyle changes, and regular monitoring."

    elif "can i play sports" in msg:
        reply = "Yes, light to moderate exercise is often encouraged. Always check with your doctor before starting a new routine."

    elif "hi" in msg or "hello" in msg or "hey" in msg:
        reply = "Hello! I’m NephroBot. Ask me anything about CKD (Chronic Kidney Disease)."
    elif "can ckd cause swelling" in msg:
        reply = "Yes, swelling in legs, ankles, or around the eyes is common in CKD due to fluid retention."

    elif "how is ckd diagnosed" in msg:
        reply = "CKD is diagnosed using blood tests (e.g., creatinine, GFR), urine tests (protein levels), and imaging."

    elif "who is at risk of ckd" in msg:
        reply = "People with diabetes, high blood pressure, heart disease, or a family history of kidney problems are at risk."

    elif "is ckd fatal" in msg:
        reply = "CKD can become life-threatening in later stages if untreated, especially if it leads to kidney failure."

    elif "stage 1 ckd" in msg:
        reply = "Stage 1 CKD means kidney damage with normal GFR (90+). It’s often asymptomatic and requires monitoring."

    elif "stage 2 ckd" in msg:
        reply = "Stage 2 CKD shows mild loss of kidney function (GFR 60–89). Lifestyle changes help slow progression."

    elif "stage 3 ckd" in msg:
        reply = "Stage 3 CKD has moderate damage (GFR 30–59). Symptoms may appear. Diet and medication are crucial."

    elif "stage 4 ckd" in msg:
        reply = "Stage 4 CKD is severe (GFR 15–29). You may prepare for dialysis or transplant. Close medical care is required."

    elif "stage 5 ckd" in msg:
        reply = "Stage 5 CKD (GFR <15) is kidney failure. Dialysis or transplant is usually necessary."

    elif "what is egfr" in msg:
        reply = "eGFR (estimated Glomerular Filtration Rate) shows how well your kidneys filter waste. Below 60 indicates CKD."

    elif "what is creatinine" in msg:
        reply = "Creatinine is a waste product in blood removed by kidneys. High levels may signal kidney dysfunction."

    elif "urine foamy" in msg:
        reply = "Foamy urine can indicate protein in urine, a possible sign of kidney damage."

    elif "ckd prevention" in msg:
        reply = "Prevent CKD by managing blood sugar, blood pressure, staying hydrated, avoiding NSAIDs, and routine checkups."

    elif "can ckd cause fatigue" in msg:
        reply = "Yes, CKD can cause fatigue due to anemia or waste buildup in the blood."

    elif "ckd blood pressure" in msg:
        reply = "High blood pressure can both cause and result from CKD. Managing BP is essential."

    elif "can ckd cause itching" in msg:
        reply = "Yes, itching or dry skin is common in CKD due to toxin buildup."

    elif "ckd and anemia" in msg:
        reply = "CKD may reduce red blood cell production, causing anemia. Treatment includes iron, EPO injections, or diet."

    elif "how to slow ckd" in msg:
        reply = "Control blood pressure, diabetes, eat healthy, avoid smoking, and take prescribed medications."

    elif "how much water" in msg:
        reply = "Water needs vary by stage and fluid retention. Don't overdrink. Follow your doctor’s advice."

    elif "should i avoid salt" in msg:
        reply = "Yes, a low-sodium diet helps prevent fluid retention and control blood pressure."

    elif "phosphorus foods" in msg:
        reply = "Limit foods like cheese, nuts, colas, and processed meats to reduce phosphorus intake in CKD."

    elif "potassium control" in msg:
        reply = "High potassium can be dangerous in CKD. Avoid bananas, oranges, tomatoes, and consult your doctor."

    elif "what is nephrologist" in msg:
        reply = "A nephrologist is a kidney specialist who manages CKD and related conditions."

    elif "can ckd be reversed" in msg:
        reply = "Most CKD is not reversible, but early intervention can stop or slow progression."

    elif "can i drink coffee" in msg:
        reply = "Moderate coffee is usually okay in CKD, but avoid high sodium/sugar creamers and stay hydrated."

    elif "ckd and diabetes" in msg:
        reply = "Diabetes is a leading cause of CKD. Blood sugar control is critical to prevent kidney damage."

    elif "ckd and pregnancy" in msg:
        reply = "Pregnancy in CKD patients needs high-risk care. Discuss with both a nephrologist and gynecologist."

    elif "how often test kidney" in msg:
        reply = "CKD patients typically test kidney function every 3–6 months depending on stage and symptoms."

    elif "can i take painkillers" in msg:
        reply = "Avoid NSAIDs like ibuprofen in CKD. Use acetaminophen if needed and consult your doctor."

    elif "how to reduce creatinine" in msg:
        reply = "Lowering creatinine means managing underlying conditions. Avoid protein overload and hydrate properly."

    elif "ckd guidelines" in msg:
        reply = "CKD care follows KDIGO guidelines focusing on GFR, albumin levels, and comorbidity control."

    elif "can i eat eggs" in msg:
        reply = "Egg whites are better than yolks in CKD. Always adjust protein intake based on stage."

    elif "can i eat chicken" in msg:
        reply = "Lean meats like chicken can be included in moderation, but portion control is key in CKD."

    elif "what is pd dialysis" in msg:
        reply = "Peritoneal dialysis uses the lining of your abdomen to filter blood. It's done at home and is an alternative to hemodialysis."

    elif "urine color ckd" in msg:
        reply = "Urine may be foamy, dark, or bloody in CKD depending on damage severity."

    elif "is ckd genetic" in msg:
        reply = "Some kidney diseases are inherited, like polycystic kidney disease, increasing CKD risk."

    elif "ckd and heart" in msg:
        reply = "CKD raises your risk of heart disease due to hypertension, fluid overload, and inflammation."

    elif "ckd and bones" in msg:
        reply = "CKD affects calcium/phosphorus balance, weakening bones and causing CKD-MBD (mineral bone disorder)."

    elif "kidney transplant" in msg:
        reply = "A kidney transplant is an option in Stage 5 CKD. It replaces the failed kidney with a healthy one."

    elif "what is urine albumin" in msg:
        reply = "Urine albumin test checks for protein leak from kidneys. High levels suggest kidney damage."

    elif "ckd diet plan pdf" in msg:
        reply = "You can generate a personalized CKD diet PDF in the Diet Plan section based on your condition."

    elif "ckd chatbot" in msg:
        reply = "You’re chatting with me now! I’m NephroBot, designed to answer your questions about CKD."

    elif "who made you" in msg:
        reply = "I was created by Samanyu Ahuja to assist users with CKD-related queries using rule-based AI."

    elif "ckd in india" in msg:
        reply = "CKD is rising in India, especially due to diabetes and hypertension. Early screening is essential."

    elif "can ckd be caused by smoking" in msg:
        reply = "Yes, smoking reduces blood flow to kidneys and worsens CKD progression."

    elif "how to stop ckd" in msg:
        reply = "CKD can’t be stopped entirely but can be slowed with lifestyle, medication, and early diagnosis."

    elif "does ckd cause back pain" in msg:
        reply = "Back pain isn’t typical in CKD unless there's a kidney infection or stones. Seek evaluation."

    elif "what is urea" in msg:
        reply = "Urea is a waste product filtered by kidneys. High levels in blood suggest poor kidney function."

    elif "ckd and depression" in msg:
        reply = "Chronic illness like CKD may lead to depression. Talk to a counselor or doctor for support."

    elif "can kids get ckd" in msg:
        reply = "Yes, children can get CKD from genetic, congenital, or acquired causes. Pediatric nephrology care is needed."

    elif "best hospital for ckd" in msg:
        reply = "Top hospitals include AIIMS, PGI Chandigarh, and Apollo. Choose one with a nephrology department."

    elif "does ckd cause headaches" in msg:
        reply = "CKD can cause headaches due to high blood pressure, anemia, or uremia."

    elif "what are kidney stones" in msg:
        reply = "Kidney stones are hard mineral deposits. They’re different from CKD but can cause damage if recurrent."

    elif "ckd vs kidney stone" in msg:
        reply = "CKD is chronic loss of kidney function. Stones are acute, often painful, and may lead to CKD if frequent."

    elif "can yoga help ckd" in msg:
        reply = "Yes, gentle yoga can improve blood flow, reduce stress, and support CKD management."

    elif "home remedies" in msg:
        reply = "Always consult a doctor. Some remedies like hibiscus tea or flaxseed are studied, but evidence is limited."

    elif "high creatinine" in msg:
        reply = "High creatinine can indicate poor kidney function. You should consult a nephrologist for further evaluation."

    elif "gfr level" in msg:
        reply = "GFR (Glomerular Filtration Rate) is a key indicator of kidney function. A GFR below 60 may suggest CKD."
    
    elif "protein in urine" in msg:
        reply = "Protein in urine (proteinuria) may indicate kidney damage. It should be investigated further."
    
    elif "bun creatinine ratio" in msg:
        reply = "An abnormal BUN/creatinine ratio could point to kidney issues or dehydration. Follow-up tests are needed."

    elif "diet for ckd" in msg:
        reply = "CKD diet includes low sodium, controlled protein, and limited potassium and phosphorus depending on stage. Always consult a renal dietitian."
    
    elif "what to eat in ckd" in msg:
        reply = "Safe foods include white rice, apples, cabbage, cauliflower, and lean protein (based on your stage and labs). Avoid salty, processed, and high-phosphorus foods."
    
    elif "ckd nutrition plan" in msg:
        reply = "A kidney-friendly plan includes small portions of protein, low-sodium options, and avoiding high potassium/phosphorus foods."
    
    elif "can i eat bananas" in msg:
        reply = "Bananas are high in potassium and may need to be limited in later CKD stages. Always check with your doctor."

    elif "how to treat ckd" in msg:
        reply = "CKD treatment includes blood pressure control, diabetes management, dietary changes, and medications to protect kidney function."
    
    elif "is ckd curable" in msg:
        reply = "CKD is not usually curable but progression can be slowed with early detection and proper management."
    
    elif "medicines for ckd" in msg:
        reply = "Common medications include ACE inhibitors, ARBs, phosphate binders, and diuretics — prescribed based on your condition."
    
    elif "dialysis" in msg:
        reply = "Dialysis is used in end-stage CKD to remove waste from the blood when kidneys stop working effectively."

    elif "what is sg" in msg:
        reply = "SG (specific gravity) measures urine concentration. Abnormal values may indicate kidney issues."
    
    elif "what is al" in msg:
        reply = "AL (albumin) in urine can signal kidney damage. High levels need medical evaluation."
    
    elif "what is rbc" in msg:
        reply = "RBC stands for red blood cells. Their presence in urine may indicate kidney inflammation or damage."
    
    elif "what is sc" in msg:
        reply = "SC (serum creatinine) is a waste product used to assess kidney function."

    elif "ckd vs aki" in msg:
        reply = "CKD is a gradual loss of kidney function. AKI (Acute Kidney Injury) is a sudden drop in function and may be reversible."
    
    elif "water for ckd" in msg:
        reply = "Water intake depends on your CKD stage and if you're retaining fluid. Follow your doctor’s recommendation."
    
    elif "can i exercise" in msg:
        reply = "Yes, light to moderate exercise is usually safe and beneficial for CKD, but consult your doctor first."
    
    elif "is ckd painful" in msg:
        reply = "CKD isn't usually painful, but symptoms like swelling, fatigue, or nausea can be uncomfortable."
    # Add 100+ more elifs here...
    
    else:
        reply = "Sorry, I didn't understand that. Try asking about CKD symptoms, treatment, diet, risk factors, or prevention."

    return jsonify({"reply": reply})


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
symptom_map = {
    "Swelling": "Pedal Edema (pe)",
    "Fatigue": "Hemoglobin (hemo)",
    "High Blood Pressure": "Blood Pressure (bp)",
    "Nausea or Vomiting": "Appetite (appet)",
    "Foamy Urine": "Albumin (al)",
    "Frequent Urination at Night": "Blood Glucose Random (bgr)",
    "Pale Skin": "Anemia (ane)",
    "Shortness of Breath": "Hemoglobin (hemo)",
    "Back Pain": "Red Blood Cells (rbc)",
}
feature_insights = {
    'age': {
        'reason': 'Older age increases the risk of chronic diseases, including kidney issues.',
        'cure': 'While age itself isn’t curable, monitoring kidney function is key in elderly individuals.',
        'remedy': 'Regular checkups, hydration, and a kidney-friendly diet can help preserve function.'
    },
    'bp': {
        'reason': 'High blood pressure can damage kidney blood vessels over time.',
        'cure': 'Use antihypertensive medications and lifestyle management.',
        'remedy': 'Limit salt intake, manage stress, and maintain a healthy weight.'
    },
    'al': {
        'reason': 'Albumin in urine signals damaged kidney filtering units (glomeruli).',
        'cure': 'Treat underlying causes like diabetes or hypertension with proper medication.',
        'remedy': 'Limit protein intake and follow a kidney-safe diet.'
    },
    'su': {
        'reason': 'Sugar in urine may indicate uncontrolled diabetes, a major CKD risk factor.',
        'cure': 'Manage blood sugar through insulin or oral medication.',
        'remedy': 'Cut down sugar, monitor glucose, and eat low-glycemic foods.'
    },
    'rbc': {
        'reason': 'Red blood cells in urine can point to kidney inflammation or damage.',
        'cure': 'Identify and treat the underlying cause such as infection or trauma.',
        'remedy': 'Drink adequate water and avoid high-impact physical activities temporarily.'
    },
    'pc': {
        'reason': 'Presence of pus cells may suggest urinary tract infection or inflammation.',
        'cure': 'Antibiotic treatment based on infection type is necessary.',
        'remedy': 'Stay hydrated and maintain good hygiene.'
    },
    'bgr': {
        'reason': 'High blood glucose is a hallmark of diabetes, which harms kidneys over time.',
        'cure': 'Insulin or oral medication to manage blood sugar.',
        'remedy': 'Avoid sweets, white rice, and soda. Exercise daily.'
    },
    'bu': {
        'reason': 'Elevated blood urea suggests reduced kidney filtering efficiency.',
        'cure': 'Manage underlying kidney issues and limit protein intake.',
        'remedy': 'Eat less red meat and processed protein. Stay hydrated.'
    },
    'sc': {
        'reason': 'High serum creatinine indicates decreased kidney function.',
        'cure': 'Depends on severity: lifestyle change or dialysis in advanced stages.',
        'remedy': 'Avoid red meat, exercise moderately, and drink water.'
    },
    'sod': {
        'reason': 'Abnormal sodium can cause blood pressure and fluid balance issues.',
        'cure': 'Adjust sodium intake and monitor electrolyte levels regularly.',
        'remedy': 'Limit processed and salty foods.'
    },
    'pot': {
        'reason': 'High potassium levels (hyperkalemia) may result from poor kidney clearance.',
        'cure': 'Use potassium binders and adjust medications as advised.',
        'remedy': 'Avoid high-potassium foods like bananas and potatoes.'
    },
    'hemo': {
        'reason': 'Low hemoglobin often signals anemia in CKD patients.',
        'cure': 'Use iron, B12, or erythropoietin based on deficiency.',
        'remedy': 'Eat iron-rich foods like spinach, lentils, or fortified cereals.'
    },
    'wbcc': {
        'reason': 'High white blood cell count may mean infection or inflammation.',
        'cure': 'Use antibiotics if bacterial infection is confirmed.',
        'remedy': 'Improve immunity with rest, hydration, and hygiene.'
    },
    'htn': {
        'reason': 'Hypertension stresses kidneys, accelerating CKD progression.',
        'cure': 'Antihypertensive drugs and lifestyle therapy are key.',
        'remedy': 'Low-salt diet, daily walks, and stress control.'
    },
    'dm': {
        'reason': 'Diabetes is a leading cause of kidney disease due to sugar damage.',
        'cure': 'Glycemic control using insulin or drugs like metformin.',
        'remedy': 'Low-carb diet, regular exercise, and glucose monitoring.'
    },
    'appet': {
        'reason': 'Poor appetite is common in CKD due to toxin buildup.',
        'cure': 'Treat nausea, acidosis, and anemia to improve appetite.',
        'remedy': 'Eat small frequent meals and avoid salty/fatty foods.'
    },
    'pe': {
        'reason': 'Pedal edema (swelling in legs) indicates fluid retention due to CKD.',
        'cure': 'Use diuretics and restrict fluid and salt intake.',
        'remedy': 'Elevate legs, reduce salt, and monitor body weight daily.'
    },
    'ane': {
        'reason': 'Anemia occurs when kidneys fail to produce enough erythropoietin.',
        'cure': 'Iron therapy, ESA injections, and correcting deficiencies.',
        'remedy': 'Consume iron and B12-rich foods like eggs and greens.'
    },
    'bun_sc_ratio': {
        'reason': 'A high BUN/Creatinine ratio can indicate dehydration or acute kidney issues.',
        'cure': 'Treat dehydration or underlying renal cause.',
        'remedy': 'Drink water regularly and avoid excess protein temporarily.'
    },
    'high_creatinine': {
        'reason': 'This binary feature flags dangerously high creatinine levels.',
        'cure': 'Advanced treatment may include dialysis.',
        'remedy': 'Consult a nephrologist immediately and monitor GFR.'
    },
    'hemo_bu': {
        'reason': 'This interaction shows combined effect of low hemoglobin and high urea — a risk signal.',
        'cure': 'Treat anemia and reduce urea levels with meds and diet.',
        'remedy': 'Focus on kidney-safe, iron-rich, low-protein meals.'
    }
}
def get_feature_insight(feature):
    return feature_insights.get(feature, {
        'reason': 'No interpretation available for this feature.',
        'cure': 'Consult a medical professional for treatment.',
        'remedy': 'Maintain a healthy lifestyle and seek expert advice.'
    })
def assess_risk(probability):
    if probability < 0.3:
        return ("Low Risk", "success")        # green
    elif probability < 0.6:
        return ("Moderate Risk", "warning")   # orange
    elif probability < 0.85:
        return ("High Risk", "danger")        # red-orange
    else:
        return ("Very High Risk", "danger")   # red
# 🔍 Define feature-specific diet sets
def get_food_sets(feature):
    db = {
        "sc": (["Cauliflower", "Berries", "Garlic", "Cabbage"], ["Red meat", "Dairy", "Shellfish"]),
        "pot": (["Apples", "Rice", "Cucumber", "Green beans"], ["Bananas", "Oranges", "Tomatoes"]),
        "sod": (["Fresh fruits", "Rice", "Unsalted nuts"], ["Chips", "Pickles", "Canned soups"]),
        "hemo": (["Spinach", "Lentils", "Pumpkin seeds", "Tofu"], ["Sugary drinks", "Alcohol"]),
        "bu": (["Egg whites", "Apples", "Zucchini", "Cauliflower"], ["Red meat", "Beans", "Cheese"]),
        "age": (["Cabbage", "Carrots", "Whole grains"], ["Processed snacks", "Cola", "Fast food"]),
        "bp": (["Leafy greens", "Berries", "Oats"], ["Salted foods", "Fried snacks"]),
        "al": (["Low-protein foods", "Fruits"], ["Red meat", "High-protein items"]),
        "su": (["Low-sugar fruits", "Watermelon"], ["Sugary drinks", "Candy"]),
        "bgr": (["Green vegetables", "Nuts", "Beans"], ["Sugary foods", "White bread"]),
        "wbcc": (["Cucumber", "Spinach", "Apple"], ["Alcohol", "Spicy food"]),
        "rbcc": (["Dates", "Raisins", "Iron-fortified cereal"], ["Fatty food"]),
        "appet": (["Small frequent meals", "Broth", "Boiled vegetables"], ["Fried food"]),
        "pe": (["Fiber-rich food", "Water"], ["Fatty spicy food"]),
        "ane": (["Beetroot", "Pomegranate", "Iron-rich food"], ["Refined sugar"])
    }
    return db.get(feature, (["Whole grains", "Cabbage"], ["Salted snacks", "Processed food"]))
# Combine diets from top 3 features
def get_diet_plan_from_features(features):
    eat_set, avoid_set = set(), set()
    for feat in features:
        eats, avoids = get_food_sets(feat)
        eat_set.update(eats)
        avoid_set.update(avoids)

    eat_list = sorted(eat_set)
    avoid_list = sorted(avoid_set)
    veg_version = eat_list.copy()
    nonveg_version = eat_list + ["Eggs", "Chicken", "Fish"]
    return veg_version, nonveg_version, avoid_list
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
    risk_level_text, risk_color = assess_risk(proba[0])
    # SHAP Analysis
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_scaled)

    # Top 4 SHAP features
    shap_abs = np.abs(shap_values[1])  # assuming class 1 is CKD
    shap_sum = shap_abs.sum(axis=0)
    top_indices = np.argsort(shap_sum)[::-1][:4]
    top_features = [X_input_df.columns[i] for i in top_indices]
    insights = []
    veg, nonveg, avoid = get_diet_plan_from_features(top_features)
    
    for feat in top_features:
        info = get_feature_insight(feat)
        info["feature"] = feat
        insights.append(info)

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
                           pdp_plot=pdp_plot_path,
                           lime_plot=lime_plot_path,
                           insights=insights,
                           diet_eat=veg,
                           diet_nonveg=nonveg,
                           diet_avoid=avoid,
                           top3=top_features,
                           risk_label=risk_level_text,
                           risk_class=f"alert-{risk_color}",
                           symptom_map=symptom_map)




@app.route('/download-diet')
def download_diet():
    eat = request.args.getlist('eat')
    avoid = request.args.getlist('avoid')
    top3 = request.args.getlist('top3')
    diet_type = request.args.get('type', 'veg')

    html = render_template('diet_pdf.html', eat=eat, avoid=avoid, top3=top3, diet_type=diet_type)

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("utf-8")), dest=result)

    if not pdf.err:
        response = make_response(result.getvalue())
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = "attachment; filename=diet_plan.pdf"
        return response
    else:
        return "❌ Failed to generate PDF", 500


@app.route('/diet')
def diet():
    eat = request.args.getlist("eat")
    nonveg = request.args.getlist("nonveg")
    avoid = request.args.getlist("avoid")
    top3 = request.args.getlist("top3")

    if not eat or not avoid or not top3:
        return render_template("diet.html", prediction_made=False)

    return render_template("diet.html",
                           prediction_made=True,
                           diet_eat=eat,
                           diet_nonveg=nonveg,
                           diet_avoid=avoid,
                           top3=top3)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
