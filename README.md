<div align="center">

# 🚀 NIFTY-50 Delta-Meta Forecaster
**A Delta-Transformation-Based Meta-Learning Hybrid Ensemble Framework**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org)
[![CI/CD Tests](https://github.com/skandanadig/delta-meta-ensembles/actions/workflows/tests.yml/badge.svg)](https://github.com/skandanadig/delta-meta-ensembles/actions)
[![Conference](https://img.shields.io/badge/Accepted-ICon%20INDIA%202026-brightgreen)](#-publications--acknowledgements)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

*An advanced, publication-grade deep learning architecture designed to tackle the volatile, non-linear, and non-stationary nature of the NIFTY-50 financial index.*

</div>

---

## 🌟 Executive Summary

Stock price prediction is notoriously difficult due to the volatile, non-stationary nature of financial markets. Traditional deep learning sequence models often fail during aggressive market trends, suffering from severe extrapolation errors and lagging predictions (failing to anticipate turning points).

**The NIFTY-50 Delta-Meta Forecaster** solves this by mapping the entire forecasting pipeline into **Delta-Space**. Instead of forcing models to guess absolute price levels they have never seen during training, our models predict the *relative change* (delta) from the previous day. This mathematically bounds the target variable into a stationary distribution, eliminating extrapolation failures and allowing the final reconstructed price series to actively track momentum and critical market reversals.

---

## 🧠 Architecture: The Hybrid Ensemble

Our framework utilizes a heterogeneous two-layer stacked ensemble, optimized for time-series forecasting.

```text
             NIFTY-50 Prices
                    ↓
             Delta Transform
                    ↓
        ┌───────────┼───────────┐
       LSTM        CNN         TCN
        └───────────┼───────────┘
                    ↓
              Meta Features
                    ↓
          Meta-Learner Ensemble
                    ↓
             Price Forecast
```

### Layer 1: Base Learners in Delta-Space
- 🌀 **LSTM (Long Short-Term Memory):** Captures temporal, long-term sequential dependencies.
- 🖼️ **CNN (Convolutional Neural Network):** Extracts local geometric and structural patterns within the time window.
- 🕰️ **TCN (Temporal Convolutional Network):** Leverages dilated causal convolutions to map long-range dependencies without the vanishing gradient problems of traditional RNNs.

### Layer 2: Meta-Learning Correction
The predictions from the base learners are fed into a meta-learner layer. We evaluated 13 different algorithms (including Random Forests, XGBoost, Ridge, and Stacking Regressors) to dynamically weigh and correct the base learner outputs, generating the final highly-accurate forecast.

---

## 🏆 Key Experimental Findings

Our experiments yielded several critical insights into deep learning for financial forecasting.

### 1. The Winning Configuration
The **E2 (LSTM + TCN)** ensemble paired with a **Random Forest meta-learner** achieved a massive **~48.7% reduction in RMSE** compared to the best standalone base model (CNN).
- 🎯 **$R^2$ Score:** `0.98892`
- 📉 **RMSE:** `0.009108` (MinMax scaled)
- 🎯 **MAPE:** `0.942%`

**Final Reconstruction Visualization:**
![Final Reconstruction](results/figures/visual_result_11.png)

### 2. Ablation Study: Absolute vs. Delta Transformation
To prove that the delta-transformation is the true driver of accuracy, we compared a linear meta-learner trained on standard absolute prices against one trained in delta-space.

The delta-transformed models demonstrated near-perfect variance explanation (jumping from an $R^2$ of ~0.81 up to **~0.988**) and massive reductions in both MSE and RMSE. Furthermore, in delta-space, shallow linear models and tree-ensembles consistently outperformed complex gradient boosting, highlighting that stabilizing the target distribution simplifies the learning objective.

![Delta vs No Delta Transformation](results/figures/delta_vs_no_delta_table.png)

### 3. Robustness: Static vs. Walk-Forward Optimization
Financial models often suffer from concept drift, requiring constant retraining (Walk-Forward Optimization). We tested our static delta approach (trained once) against a dynamic walk-forward approach (rolling refits) to evaluate robustness over time.

**The result:** The performance difference was negligible (often <2% change in error). The Delta-Transformation inherently stabilizes the distribution so well that frequent, computationally expensive meta-learner retraining becomes unnecessary for live-trading scenarios.

![Walk-Forward vs Static Delta Table](results/figures/walk_forward_table.png)

*The plots below show that despite the Walk-Forward model dynamically adjusting base-learner weights over time, the Rolling RMSE remains nearly identical to the highly efficient Static model.*
![Walk-Forward vs Static Delta Graphs](results/figures/walk_forward_graphs.png)

---

## 🚀 Interactive Notebooks

Want to experiment with the data and models immediately? You can run the complete pipeline directly in Google Colab:
- [Previous Version (Initial Setup & Exploration)](https://colab.research.google.com/drive/1645Yj1u76I2qkI8xb82Mr2gnyR6VAaqH)
- [Version After 3 Reviews (Final Version with Additional Tests)](https://colab.research.google.com/drive/1645Yj1u76I2qkI8xb82Mr2gnyR6VAaqH#scrollTo=9YHULAkwd4ZB)

---

## 📂 Repository & Reproducibility

This project is architected as a professional, reproducible ML software system.

```text
📦 nifty50-forecasting
 ┣ 📂 configs               # YAML configs for hyperparameters
 ┣ 📂 data                  # Raw and processed datasets
 ┣ 📂 notebooks             # Jupyter/Colab prototyping environments
 ┣ 📂 paper                 # Standalone research manuscript PDF
 ┣ 📂 results               # Metrics, ablation results, and saved figures
 ┣ 📂 src                   # Core package (models, data pipelines, training)
 ┗ 📂 tests                 # Unit tests for data logic (pytest)
```

### Getting Started Locally

**1. Clone the repository**
```bash
git clone https://github.com/skandanadig/delta-meta-ensembles.git
cd delta-meta-ensembles
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
# OR install as a package:
pip install -e .[dev]
```

**3. Run the Training Pipeline**
The system is fully configurable via YAML:
```bash
python -m src.train --config configs/ensemble.yaml
```

---

## 🎓 Publications & Acknowledgements

This research was conducted as an internship project at the **Center for Cloud Computing and Big Data (CCBD), PES University**.

> 🎉 **Publication Accepted!**  
> This paper has been officially accepted for presentation at **The International Conference on Intelligent Networks and Data-driven Intelligent Applications (ICon INDIA 2026)**, scheduled for **20–22 November 2026 in Puducherry, India**.

### 👥 Contributors
- **Skanda Shyam Nadig** - *PES University*
- **Sharat Doddihal** - *PES University*
- **Shishir Hegde** - *PES University*
- **Shree Verdhan M** - *PES University*
- **Dr. Nagegowda K S** - *Professor, PES University*

<div align="center">
<i>Crafted with ❤️ for Quantitative Finance, Machine Learning, and Academic Excellence.</i>
</div>
