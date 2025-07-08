# ckdinterface
NephroCare: CKD Risk Assessment and Guidance Platform

NephroCare is a web-based application designed to help users assess the risk of Chronic Kidney Disease (CKD) using a machine learning model. It provides a user-friendly interface for medical data input, predictive analysis, model explainability through SHAP, LIME, PDP plots, and AI-generated diet recommendations.

⸻

Features
	•	Upload or manually enter patient medical data
	•	CKD prediction using a trained Random Forest model
	•	Probability score for CKD presence or absence
	•	SHAP and LIME explainability visualizations
	•	Partial Dependence Plot (PDP) for feature influence
	•	AI-generated report and recommendations
	•	Clean Bootstrap-based frontend with dark mode toggle
	•	Integrated chatbot and language toggle support

⸻

Tech Stack
	•	Frontend: HTML, CSS, Bootstrap 5, JavaScript
	•	Backend: Python, Flask
	•	ML Libraries: Scikit-learn, SHAP, LIME, matplotlib, pandas, numpy
	•	Deployment Ready: Render, Railway, Netlify (for static), AWS

 Folder Structure
 /
├── app.py                       # Flask backend logic
├── models/                     # Pre-trained models and scaler
│   ├── rf_model_final.pkl
│   ├── scaler_final.pkl
│   └── X_train_res_scaled.pkl
├── static/
│   ├── plots/                  # SHAP and PDP plots
│   ├── style.css               # Global styling
│   └── scripts.js              # JS for chatbot and interactions
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── diagnosis.html
│   ├── diet.html
│   ├── result.html
│   ├── chatbot.html
│   └── language.html
├── requirements.txt            # Python dependencies
├── Procfile                    # Deployment startup config
└── README.md

Requirements
