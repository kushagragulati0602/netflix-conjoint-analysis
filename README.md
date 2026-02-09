# 🎬 Netflix Consumer Choice Analysis

**A polished, product-style conjoint simulation & interactive dashboard (Streamlit + Python)**  
Simulate consumer subscription choices, visualize part-worth utilities, and test plan concepts to estimate market-share impact. This repo demonstrates an end-to-end product-analytics workflow — from synthetic data and encoded part-worths → interpretation → market simulation — packaged as an interactive Streamlit app you can run locally.

---

## 🚀 TL;DR

An interactive demo that lets you:
- Inspect attribute importance and part-worth utilities for subscription features (Price, Ads, Quality, Screens).  
- Configure two competing plan concepts and immediately see predicted market shares using a logit-based model.  
- Translate preference signals into actionable pricing & product recommendations.

This project is intended for product managers, growth analysts, and data-savvy PMs who want a demo-quality decision tool for pricing and tier design.

---

## ✨ Key features

- **Attribute importance dashboard** — which features move the needle.  
- **Part-worth utility charts** — interpretable marginal utilities across levels.  
- **Interactive market simulator** — configure Baseline vs. New Concept, get predicted market share (multinomial logit / softmax).  
- **Actionable strategic insights** — built-in takeaways and a sample recommendation (“Goldilocks” mid-tier).  
- **Product-grade UI** — Streamlit app with clear navigation and responsive charts.

---

## ⚠️ Important methodology note (be transparent)

- The app uses **synthetic data** and **pre-defined part-worth utilities** (encoded in `TRUE_UTILITIES`) to produce realistic, interpretable outputs.  
- Market-share predictions use a **multinomial logit (softmax)** on summed utility values.  
- **This is a demonstration/portfolio tool** for interpretation and product strategy — it does **not** perform Hierarchical Bayes estimation on real survey responses. If you need estimation from real conjoint data, see the "Extensions" section.

---

## 🔧 Quickstart — run locally (copy & paste)

```bash
# 1. Clone repo
git clone https://github.com/kushagragulati0602/netflix-conjoint-analysis.git
cd netflix-conjoint-analysis

# 2. (Recommended) Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate       # Windows PowerShell

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
