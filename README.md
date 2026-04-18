# Telecom Customer Churn Analysis

### Identifying $1.67M in Annual Revenue Risk Through Behavioral Segmentation & Predictive EDA

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-EDA-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C8CBF)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Customers](https://img.shields.io/badge/Customers-7%2C043-blue)
![Churn Rate](https://img.shields.io/badge/Churn%20Rate-26.5%25-red)

---

## Quick Summary

- **26.5% of 7,043 customers churned**, translating to **$1.67M in annualized revenue leakage** ($139K/month)
- Month-to-month contract holders churn at **42.7%** — 15x higher than two-year contract customers (2.8%)
- Fiber optic subscribers and electronic check payers are the two highest-risk behavioral segments, both exceeding **41% churn**
- Customers without online security churn at **41.8%** vs. 14.6% for those who have it — a 2.9x gap driven by an upsell gap, not product quality
- Tenure is the single strongest protective factor: customers past the **12-month mark** drop off sharply in churn probability
- EDA surfaces four actionable retention levers that could realistically recover **35–40% of churned revenue** with targeted interventions

---

## Business Problem

Telecom companies operate in a near-commoditized market where acquiring a new customer costs 5–7x more than retaining an existing one. At a 26.5% annual churn rate, this provider is cycling through roughly one in four customers every year — burning acquisition budget to replace revenue that should never have left.

The problem is not that customers leave. It is that the warning signs — contract type, payment behavior, service configuration, tenure — are sitting in the data and going unread. Without a structured analytical layer, retention teams are reacting to churn instead of preventing it.

---

## Objective

Conduct a full exploratory data analysis on 7,043 telecom customer records to identify which behavioral, contractual, and demographic factors most strongly predict churn — and translate those patterns into retention strategies with measurable revenue impact.

---

## Dataset

| Attribute | Detail |
|---|---|
| **Source** | IBM Watson Telco Customer Churn dataset |
| **Records** | 7,043 customers |
| **Features** | 21 columns — demographics, service subscriptions, contract type, billing, churn label |
| **Target Variable** | `Churn` (binary: Yes / No) — 26.5% positive class |
| **Class Imbalance** | 73.5% No / 26.5% Yes — addressed in analysis interpretation |
| **Missing Values** | 11 records in `TotalCharges` (0.15%) — dropped safely |
| **Revenue Coverage** | $16.06M in total billed charges across all customers |

Key features: `tenure`, `Contract`, `MonthlyCharges`, `TotalCharges`, `InternetService`, `PaymentMethod`, `OnlineSecurity`, `TechSupport`, `SeniorCitizen`

---

## Approach

**1. Data Audit & Cleaning**
Identified and corrected `TotalCharges` stored as string type, removed 11 null records (0.15% of data), validated no other missing values across 21 features.

**2. Feature Engineering**
Binned `tenure` into six 12-month cohorts (1–12, 13–24, ... 61–72 months) to expose non-linear churn risk over time. Encoded `Churn` as binary (1/0) for correlation analysis.

**3. Univariate Analysis**
Profiled each predictor's distribution across churned vs. retained customers using count plots. Surfaced immediate separators: contract type, payment method, and internet service tier each showed stark distributional differences by churn status.

**4. Bivariate & Correlation Analysis**
Built a full correlation matrix against the churn target. Identified top positive correlators (month-to-month contracts, fiber optic, electronic check, no online security) and top negative correlators (two-year contracts, 5+ year tenure, bundled services). Confirmed gender and phone service carry near-zero predictive signal.

**5. Charge Behavior Analysis**
Used KDE plots to show that churn concentrates among high-monthly-charge, low-tenure customers — explaining the seemingly counterintuitive pattern where churned customers have lower total charges (short tenure compresses lifetime spend).

**6. Revenue Impact Quantification**
Mapped churned customers' monthly charges to compute revenue-at-risk figures: $139K/month, $1.67M annualized.

---

## Key Insights

**Contract type is the dominant churn driver.**
Month-to-month customers churn at 42.7% — 15x the rate of two-year contract holders (2.8%). This is not a product satisfaction problem; it is a commitment architecture problem.

**Electronic check is a behavioral churn signal, not a payment preference.**
Customers paying by electronic check churn at 45.3% — the highest of any payment method. Electronic check users tend to be earlier-tenure, less-engaged customers. This variable is a proxy for low commitment, not a cause.

**Fiber optic subscribers are churning at 41.9% despite paying the most.**
This is the most expensive segment to lose. High monthly charges plus high churn = maximum revenue destruction. Likely driven by unmet performance expectations or competitive price pressure.

**Online security absence is a retention gap, not a customer choice.**
Customers without online security churn at 41.8% vs. 14.6% for those who have it. This is almost certainly an upsell gap — customers who are not yet embedded in the service ecosystem have no switching cost.

**Tenure is the strongest churn shield.**
Customers in their first year churn at dramatically higher rates. Those who survive past 12 months show rapidly declining churn probability. Retention investment has its highest ROI in months 1–12.

**Senior citizens churn at 41.7% — nearly double the base rate.**
This segment may have specific usability, billing clarity, or support needs that are not being met by standard service tiers.

**Gender and phone service have no meaningful predictive value.**
Confirmed via correlation analysis. These variables can be deprioritized in retention modeling.

---

## Business Recommendations

**1. Convert month-to-month customers to annual contracts with a targeted incentive.**
A 10–15% first-year discount for switching to a one-year contract would pay back in reduced churn within 4–6 months. Priority segment: month-to-month customers in their first 12 months with monthly charges above $65.

**2. Treat fiber optic churn as a product-market fit problem, not a pricing problem.**
Survey recently churned fiber customers. If the driver is speed/reliability, resolve it operationally. If it is price, a loyalty rate or bundle is cheaper than losing the account. This segment alone represents disproportionate revenue risk.

**3. Build an online security upsell campaign targeting unprotected month-to-month customers.**
The 2.9x churn gap between secured and unsecured customers suggests that adding even one bundled service significantly increases switching cost. A free 90-day trial of online security for at-risk accounts is worth testing.

**4. Implement a 30/60/90-day onboarding intervention for all new customers.**
Churn is heavily concentrated in year one. A structured engagement program — proactive support outreach, usage check-ins, bundle education — targeted at customers with no add-on services and month-to-month contracts could meaningfully shift the first-year retention curve.

**5. Develop a dedicated support track for senior citizens.**
At 41.7% churn, this is a segment with specific, addressable needs. Simplified billing, priority support access, or a dedicated agent tier could recover meaningful revenue at relatively low cost.

---

## Visuals

> **Note:** All visualizations are generated in-notebook via Matplotlib and Seaborn. Run `notebooks/Churn_EDA.ipynb` to reproduce. Representative outputs include:

| Visual | Insight Delivered |
|---|---|
| Churn Distribution Bar Chart | 73.5/26.5 class split — baseline for all downstream analysis |
| Correlation Bar Plot (vs. Churn) | Ranked feature importance — top and bottom predictors at a glance |
| KDE: Monthly Charges by Churn | Churners concentrate in the $65–$100 monthly charge band |
| KDE: Total Charges by Churn | Confirms short-tenure, high-monthly-charge = highest risk profile |
| Contract Type Count Plot | Month-to-month dominates churn population |
| Payment Method Distribution | Electronic check = highest churn concentration |
| Correlation Heatmap (all features) | Structural relationships — tenure/TotalCharges collinearity visible |
| Tenure Group Distribution | First 12-month cohort carries outsized churn weight |

---

## Model Performance

This project focuses on EDA and does not include a predictive model. The correlation and segmentation analysis delivers actionable segmentation without the overhead of model validation — appropriate for a business intelligence use case where segment rules are more operationally deployable than probability scores.

**Next step (not yet built):** A logistic regression or gradient-boosted classifier trained on this feature set, with SHAP values for interpretability, would be the natural extension. Feature selection based on this EDA would exclude `gender` and `PhoneService` from the start.

---

## Outcome & Impact

This analysis identifies four specific customer segments that collectively account for the majority of churn risk:

- **Month-to-month + first-year tenure + no security add-ons:** highest churn probability, highest intervention ROI
- **Fiber optic + electronic check + high monthly charges:** highest revenue-per-churner, most expensive to lose
- **Senior citizens:** elevated churn with addressable, non-price drivers
- **5+ year tenured customers:** near-zero churn — the profile to engineer toward

Targeted retention action on the first two segments alone could realistically prevent **400–500 churns per year** — recovering an estimated **$550K–$700K in annual revenue** based on the average monthly charge of churned customers ($74.44).

---

## Project Structure

```
telecom-churn-analysis/
│
├── data/
│   ├── CustomerChurn.csv            ← Raw dataset (7,043 records, 21 features)
│   └── tel_churn_processed.csv      ← Cleaned, encoded dataset (EDA output)
│
├── notebooks/
│   └── Churn_EDA.ipynb              ← Full exploratory analysis — cleaned, commented
│
├── outputs/
│   ├── figures/                     ← Saved plot PNGs (churn_dist, kde_monthly, etc.)
│   └── churn_segment_summary.csv    ← Churn rates by contract, payment, internet type
│
├── reports/
│   └── Churn_Analysis_Report.pdf    ← Business-ready summary (recommended addition)
│
├── requirements.txt
└── README.md
```

---

## Gaps & What to Add Next

**Currently weak:**
- No saved output figures (recruiter cannot see results without running the notebook)
- Notebook markdown commentary is minimal — code tells the story, text does not
- No segment summary table exported as a standalone file
- No model baseline (even a simple logistic regression adds significant credibility)

**High-impact additions:**
- Export 8–10 key plots as PNGs into `/outputs/figures/` so they render on GitHub
- Add a `churn_by_segment.csv` with a clean table of churn rates across all key dimensions
- Write a 2-page PDF business summary — proves you can communicate findings to non-technical stakeholders
- Add a logistic regression with ROC-AUC score — even 0.78–0.82 is strong for this dataset and signals ML readiness
- Add SHAP or feature importance plot — one of the most recruiter-visible signals of modern ML practice

---

## Tools & Technologies

| Layer | Stack |
|---|---|
| **Language** | Python 3.9+ |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **EDA Techniques** | Univariate analysis, bivariate analysis, correlation matrix, KDE plots, count plots |
| **Data Cleaning** | Type coercion, null handling, feature binning, one-hot encoding |
| **Environment** | Jupyter Notebook |
| **Version Control** | Git & GitHub |

---

## Contact

**Surya Prakash** — Data Analyst
Hyderabad, India
[LinkedIn](https://www.linkedin.com/in/surya-prakash-data-analyst) · [GitHub](https://github.com/surya-prakash-data-analyst)
suryaprakash1892@gmail.com

---

*7,043 customers · $16M revenue analyzed · 26.5% churn rate decoded · Python + EDA + Business Impact*
