# A Delta-Transformation-Based Meta-Learning Hybrid Ensemble Framework for NIFTY-50 Index Forecasting

> [!NOTE]
> Please upload your actual `.pdf` manuscript to this folder so it can be easily accessed. Below is a text summary/transcript of the paper for quick reference.

**Authors:** Sharat Doddihal, Shishir Hegde, Skanda Shyam Nadig, Shree Verdhan M, Dr Nagegowda K S (PES University)

## Abstract
Stock Price Prediction is a complex challenge in the field of finance due to its inherent volatility and its non-linear, and non-stationary nature. Current Statistical and Machine Learning models struggle to capture non-linear and non stationary patterns. Stacked ensembles improve prediction performance but struggle with distribution shifts and poor extrapolation when the market moves beyond the training range. In this study, we train and evaluate three base models (LSTM, CNN, and TCN) on historical NIFTY 50 OHLC data sourced from Yahoo Finance. These are combined into two ensemble architectures: LSTM+CNN and LSTM+TCN. Their predictions are transformed into delta space, and then 13 meta-learners are systematically evaluated to find the most effective ensemble architecture.Furthermore, three feature scaling techniques: MinMax, Standard, and Robust Scaling are compared, and the robustness of the proposed framework is evaluated using five-fold cross-validation. Experimental results show improved robustness, higher $R^2$ and lower prediction errors.

## I. Introduction
Anticipating financial market movements is critical in the field of quantitative finance, algorithmic trading, index fund management and hedging. Accurate forecasts provide essential strategic value to portfolio managers, retail investors, and regulatory bodies. A formidable challenge in accurate price prediction arises from the stochastic, highly volatile and non-stationary behavior of equity markets.

To effectively decode the multi-dimensional nature of the NIFTY-50 index, we propose a heterogeneous foundation of deep learning architectures- specifically LSTM, CNN, TCN -as independent base learners. The core strength of the Long Short-Term Memory(LSTM) network lies in its specialized gating mechanisms. One-dimensional Convolutional Neural Networks(CNNs) approach the 10-day OHLC sliding window with a spatial bias. While Temporal Convolutional Networks exhibited the weakest isolated performance, their capacity to capture long range dependencies via dilated causal convolutions generated unique predictive signals.

To mitigate price-level distribution shift, this study proposes a Delta-Transformation based meta-learning hybrid ensemble framework. Instead of training the meta-learner to predict the absolute closing price, the proposed approach transforms both the base model outputs and the true target values into price changes relative to the immediately preceding observed closing price.

## II. Methodology

### Data Acquisition and Preprocessing
The empirical analysis utilizes historical data of the NIFTY-50 index acquired via Yahoo Finance. The dataset spans an 11-year period from January 1, 2013, to January 1, 2024. The feature set comprises four daily market indicators: open, high, low, and close prices, with the close prices acting as the target variable.

The time series data is restructured using a sliding window approach with a window size of $p = 10$ days. The dataset is chronologically partitioned without shuffling into training (60%), validation (15%), and testing (25%) sets.

### Stacked Ensemble Design
To harness the strengths of the distinct neural architectures, a stacked ensemble strategy is deployed. The two primary ensemble configurations are:
1. **Ensemble 1 (E1):** LSTM + CNN
2. **Ensemble 2 (E2):** LSTM + TCN

### Delta-Space Meta-Learner Training
Rather than training the meta-learner directly on the raw predicted price levels of each base learner, both the base-learner outputs and the target are transformed into a delta space. 
$\Delta\hat{y}^{(m)}_{t+1} = \hat{y}^{(m)}_{t+1} - y_t$
The meta-learner $g(\cdot)$ is then trained to map the base-learner deltas to the target delta. During inference, the final price-level prediction is reconstructed as:
$\hat{y}_{t+1} = y_t + \Delta\hat{y}_{t+1}$

## III. Results and Conclusion

The best configuration, **E2 (LSTM+TCN) with a Random Forest meta-learner**, achieved an RMSE of 0.009108 and $R^2$ of 0.98892 on the test set, a 48.7% RMSE reduction over the best individual base model (CNN). 

The ablation study led to four main findings:
1. The choice of which two base learners are paired (LSTM+CNN vs. LSTM+TCN) has only a marginal effect once a meta-learner correction is applied.
2. Linear and hybrid-linear meta-learners (Ridge, Lasso, Stacking) consistently match or exceed most non-linear meta-learners.
3. The choice of feature scaler (MinMax, Standard, Robust) has negligible effect on $R^2$, confirming that the architecture and the delta-space reconstruction are responsible for the observed accuracy.
4. 5-fold cross-validation suggests that the broader family-level performance hierarchy remains relatively stable.

These results support a simple, low-variance design recommendation for this class of problem: a two-layer ensemble with a shallow linear (or Random Forest) meta-learner trained in delta space is generally preferable to most complex non-linear stacking architectures.
