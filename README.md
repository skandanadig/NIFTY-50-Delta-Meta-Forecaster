<div align="center">

# 🚀 NIFTY-50 Delta-Meta Forecaster
**A Delta-Transformation-Based Meta-Learning Hybrid Ensemble Framework**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

*An advanced, publication-grade deep learning architecture designed to tackle the volatile, non-linear, and non-stationary nature of the NIFTY-50 financial index.*

</div>

---

## 🌟 Project Overview

Welcome to the **NIFTY-50 Delta-Meta Forecaster**! 

Stock price prediction is notoriously difficult, especially when the market trends aggressively into unprecedented highs or lows (distribution shifts). Traditional stacked ensembles often fail when forced to extrapolate. 

**Our Solution?** We mapped the entire problem into **Delta-Space**! 🌌

Instead of forcing our models to guess absolute price levels, our base learners predict *the change relative to the previous day*. We then use a secondary **Meta-Learner** to synthesize these predictions, resulting in a model that dynamically adapts to market trends without suffering from naive lag.

---

## 🧠 The Architecture

Our framework is built on a heterogeneous **two-layer stacked ensemble**:

1. **The Base Learners:** We employ state-of-the-art Deep Learning models to extract unique temporal and spatial features from a 10-day sliding window of NIFTY-50 OHLC data.
   - 🌀 **LSTM:** Captures long-term sequential dependencies.
   - 🖼️ **CNN:** Extracts local geometric and structural patterns.
   - 🕰️ **TCN:** Leverages dilated causal convolutions for long-range mapping.
2. **The Meta-Learners:** We evaluated **13 different meta-learners** in delta-space (including Random Forest, XGBoost, Ridge, and Stacking Regressors) to find the perfect synergistic correction layer.

---

## 🏆 Key Highlights & Results

We rigorously tested our framework on **11 years of historical data (Jan 2013 - Jan 2024)**. 

> [!TIP]
> **Winner:** The **E2 (LSTM + TCN) ensemble** paired with a **Random Forest meta-learner** dominated the evaluations!

- 📉 **RMSE:** `0.009108` (MinMax scaled)
- 🎯 **$R^2$ Score:** `0.98892`
- ⚡ **Performance Leap:** A massive **~49% reduction in RMSE** compared to the best standalone base model (CNN).
- 💡 **Interesting Finding:** In delta-space, shallow linear models and tree-ensembles consistently outperformed highly complex gradient boosting and neural networks, proving that the delta-transformation itself is the true driver of accuracy!

---

## 📂 Repository Structure

Everything is cleanly organized so you can dive right in:

```text
📦 nifty50-forecasting
 ┣ 📂 data                  # Raw and processed datasets
 ┣ 📂 notebooks             # The core Jupyter Notebook containing the experiments
 ┣ 📂 paper                 # The standalone research manuscript PDF
 ┣ 📂 results               
 ┃ ┣ 📂 tabular_results     # Clean CSVs of all 7 data tables from the paper
 ┃ ┗ 📂 visual_results      # Border-trimmed screenshots of performance graphs
 ┣ 📜 README.md             # You are here!
 ┗ 📜 requirements.txt      # Python dependencies
```

---

## 🚀 Getting Started

Want to run the models yourself? It's easy!

**1. Clone the repository**
```bash
git clone https://github.com/skandanadig/delta-meta-ensembles.git
cd delta-meta-ensembles
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Fire up the Notebook!**
```bash
jupyter notebook notebooks/nifty50_forecasting.ipynb
```

---
<div align="center">
<i>Crafted with ❤️ for Quantitative Finance and Machine Learning.</i>
</div>
