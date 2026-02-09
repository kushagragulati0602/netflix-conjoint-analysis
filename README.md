# 📺 Netflix Conjoint Analysis: Optimizing Subscription Strategy

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org)
[![Analysis](https://img.shields.io/badge/Methodology-Choice--Based--Conjoint-green)](https://en.wikipedia.org/wiki/Conjoint_analysis)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Project Overview
How does Netflix decide if "4K Video" is worth a $3 price hike? This project implements **Choice-Based Conjoint (CBC) Analysis** to quantify consumer trade-offs. By analyzing survey-based choice data, we calculate the **Part-Worth Utility** of specific features and predict how different plan configurations affect market share.

### **The Business Problem**
Subscription services face a constant battle: maximizing Average Revenue Per User (ARPU) without increasing churn. This analysis identifies the "Sweet Spot" between price, content library, and technical features to optimize product tiers.

---

## 🛠️ Technical Stack
* **Data Manipulation:** `pandas`, `numpy`
* **Statistical Modeling:** `statsmodels` (Logit & Probit models), `scikit-learn`
* **Visualization:** `matplotlib`, `seaborn`
* **Core Concept:** Discrete Choice Modeling / Multinomial Logistic Regression

---

## 📊 Key Attributes Analyzed
We evaluated the following features to see which drives the most value for users:
* **Monthly Price:** $9.99, $14.99, $19.99
* **Video Quality:** SD, HD, 4K+HDR
* **No. of Screens:** 1, 2, 4
* **Content Access:** Limited vs. Full Library

---

## 🚀 Key Insights & Findings

### **1. Attribute Importance**
> **Finding:** Price is the primary driver of choice, accounting for **~42%** of the decision-making process, followed by Video Quality (**28%**).

### **2. Part-Worth Utilities**
* **Feature Value:** Users showed a disproportionately high utility for the jump from **SD to HD** compared to the jump from **HD to 4K**.
* **Price Sensitivity:** There is a significant "utility cliff" after the **$15** mark, suggesting a psychological pricing barrier for the "Standard" user segment.

### **3. Market Simulator**
Included in this repository is a **Market Simulator** that predicts the "Share of Preference" for hypothetical bundles. 
* *Scenario:* A $12.99 plan with 2 screens and HD quality outperforms a $9.99 plan with 1 screen and SD quality by **15%** in predicted preference.

---

## 📁 Repository Structure
```bash
├── data/               # Raw and cleaned survey choice sets
├── notebooks/          # Step-by-step analysis and model building
├── src/                # Modular scripts for utility & WTP calculations
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
