# Baseline training script for Customer Churn Prediction
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('../data/CustomerChurn.xls')  # file may be CSV-formatted
for c in df.select_dtypes(include=['object','category']).columns:
    df[c] = df[c].fillna('NA')
    df[c] = LabelEncoder().fit_transform(df[c].astype(str))

TARGET = 'Churn'
X = df.drop(columns=[TARGET])
y = df[TARGET]
try:
    y = y.astype(int)
except:
    y = LabelEncoder().fit_transform(y.astype(str))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train, y_train)
preds = clf.predict(X_test)
probs = clf.predict_proba(X_test)[:,1] if hasattr(clf, 'predict_proba') else None
print('Accuracy:', accuracy_score(y_test, preds))
print('F1:', f1_score(y_test, preds, average='binary' if len(pd.unique(y))==2 else 'weighted'))
if probs is not None:
    print('ROC AUC:', roc_auc_score(y_test, probs))
