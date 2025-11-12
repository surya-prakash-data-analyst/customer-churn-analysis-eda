# 📊 Customer Churn Analysis — EDA & Prediction

**Author:** Surya Prakash  
**Dataset read by:** read_csv  
**Target:** Churn

## Project Overview
This project analyzes customer churn patterns and builds a baseline predictive model to identify customers at risk of churn. Deliverables include EDA notebooks, baseline model script, visuals, and a business-focused PDF report.

## Repository Structure
```
Customer_Churn_Analysis_Project/
├── data/
│   └── CustomerChurn.xls
├── notebooks/
│   └── Churn_Analysis_EDA.ipynb
├── scripts/
│   └── train_churn_model.py
├── images/
│   ├── churn_distribution.png
│   ├── correlation_heatmap.png
│   └── feature_importance.png
├── docs/
│   └── Customer_Churn_Insights_Report.pdf
├── requirements.txt
└── README.md
```

## Quick EDA Summary
- Shape: (7043, 21)
- Missing values per column: {'customerID': 0, 'gender': 0, 'SeniorCitizen': 0, 'Partner': 0, 'Dependents': 0, 'tenure': 0, 'PhoneService': 0, 'MultipleLines': 0, 'InternetService': 0, 'OnlineSecurity': 0, 'OnlineBackup': 0, 'DeviceProtection': 0, 'TechSupport': 0, 'StreamingTV': 0, 'StreamingMovies': 0, 'Contract': 0, 'PaperlessBilling': 0, 'PaymentMethod': 0, 'MonthlyCharges': 0, 'TotalCharges': 0, 'Churn': 0}
- Data types: {'customerID': 'object', 'gender': 'object', 'SeniorCitizen': 'int64', 'Partner': 'object', 'Dependents': 'object', 'tenure': 'int64', 'PhoneService': 'object', 'MultipleLines': 'object', 'InternetService': 'object', 'OnlineSecurity': 'object', 'OnlineBackup': 'object', 'DeviceProtection': 'object', 'TechSupport': 'object', 'StreamingTV': 'object', 'StreamingMovies': 'object', 'Contract': 'object', 'PaperlessBilling': 'object', 'PaymentMethod': 'object', 'MonthlyCharges': 'float64', 'TotalCharges': 'object', 'Churn': 'object'}

## Baseline Model Metrics (auto)
{'accuracy': 0.7942, 'f1': 0.5566, 'roc_auc': 0.8286, 'n_samples': 7043, 'n_features': 20}

## How to run
1. pip install -r requirements.txt
2. jupyter notebook notebooks/Churn_Analysis_EDA.ipynb
3. python scripts/train_churn_model.py
