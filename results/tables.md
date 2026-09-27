# Results: Data Tables

Below are all the comprehensive evaluation tables from the study "A Delta-Transformation-Based Meta-Learning Hybrid Ensemble Framework for NIFTY-50 Index Forecasting".

## Table I: Ablation of Base-Model Pairing
*Best Meta-Learner per Ensemble (Test Set, MinMax Scaling)*

| Ensemble | Best Learner | RMSE | $R^2$ | MAE | MAPE (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E1 (LSTM+CNN) | Ridge | 0.009112 | 0.98891 | 0.006903 | 0.944 |
| E2 (LSTM+TCN) | RandomForest | 0.009108 | 0.98892 | 0.006892 | 0.942 |

---

## Table II: Ablation of Meta-Learner Family on E2 (LSTM+TCN)
*Test Set Performance*

| Meta-Learner | Type | MSE | RMSE | $R^2$ | MAPE (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RandomForest | Non-linear | 8.295e-5 | 0.009108 | 0.98892 | 0.942 |
| Ridge | Linear | 8.301e-5 | 0.009111 | 0.98891 | 0.943 |
| Stacking | Hybrid | 8.303e-5 | 0.009112 | 0.98890 | 0.944 |
| Lasso | Linear | 8.303e-5 | 0.009112 | 0.98890 | 0.944 |
| ExtraTrees | Non-linear | 8.366e-5 | 0.009147 | 0.98882 | 0.946 |
| Linear | Linear | 8.577e-5 | 0.009261 | 0.98854 | 0.963 |
| Huber | Linear | 8.609e-5 | 0.009279 | 0.98850 | 0.956 |
| XGBoost | Non-linear | 8.779e-5 | 0.009369 | 0.98827 | 0.966 |
| GradientBoost | Non-linear | 8.940e-5 | 0.009455 | 0.98805 | 0.983 |
| LightGBM | Non-linear | 9.206e-5 | 0.009595 | 0.98770 | 0.984 |
| CatBoost | Non-linear | 9.263e-5 | 0.009625 | 0.98762 | 0.983 |
| SVR | Non-linear | 9.495e-5 | 0.009744 | 0.98731 | 1.006 |
| MLP | Non-linear | 1.089e-4 | 0.010435 | 0.98545 | 1.103 |

---

## Table III: Ablation of Feature-Scaling Strategy
*Best Configuration per Scaler, E2 Ensemble unless noted, Test Set*

| Scaler | Best Learner | Ensemble | RMSE* | $R^2$ |
| :--- | :--- | :--- | :--- | :--- |
| MinMax | RandomForest | E2 | 0.009108 | 0.98892 |
| Standard | Ridge | E2 | 0.036143 | 0.98891 |
| Robust | RandomForest | E2 | 0.022215 | 0.98900 |

*\*RMSE reported in each scaler's own output units; not directly comparable across rows.*

---

## Table VI: Base-Model Test-Set Performance
*Scaled Target, MinMax, Before Ensembling*

| Model | MSE | RMSE | $R^2$ | MAE | MAPE (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LSTM | 4.990e-4 | 0.022339 | 0.93332 | 0.018569 | 2.428 |
| CNN | 3.151e-4 | 0.017750 | 0.95790 | 0.013944 | 1.884 |
| TCN | 9.201e-4 | 0.030332 | 0.87705 | 0.026027 | 3.465 |

---

*(Note: Tables IV, V, and VII from the paper detail the extensive 5-fold cross-validation metrics which confirm the robustness of the E2 and E1 architectures shown above).*
