# A Delta-Transformation-Based Meta-Learning Hybrid Ensemble Framework for NIFTY-50 Index Forecasting

This repository contains the code, data structures, and results for forecasting the NIFTY-50 index using a novel Delta-Transformation-Based Meta-Learning Hybrid Ensemble Framework. 

## Project Explanation & Approach

Stock price prediction is highly challenging due to non-linear and non-stationary behavior. While stacked ensembles improve predictions, they often struggle when out-of-sample data distributions shift (e.g., during sustained market trends where absolute price levels exceed anything seen in training).

To address this, our framework transforms predictions into **delta space**. Rather than predicting absolute price levels, our models predict the *change* relative to the previous day's closing price. 

**Methodology Highlights:**
1. **Base Learners:** We utilize deep learning models—Long Short-Term Memory (LSTM), Convolutional Neural Networks (CNN), and Temporal Convolutional Networks (TCN)—to capture different aspects of sequential and local structural market patterns over a 10-day OHLC sliding window.
2. **Ensemble Configurations:** We stack these models into two main configurations:
   - **E1:** LSTM + CNN
   - **E2:** LSTM + TCN
3. **Meta-Learners in Delta Space:** Base model predictions are mapped to price *deltas*, which are then passed to a secondary meta-learner. We evaluated 13 different meta-learners (Linear Regression, Ridge, Lasso, Huber, Random Forest, XGBoost, etc.) to correct base model outputs.
4. **Final Prediction:** The absolute price is reconstructed by adding the predicted delta to the previous day's observed closing price.

## Key Results

Our empirical study on 11 years of NIFTY-50 data (Jan 2013 - Jan 2024) demonstrates that delta-space ensembling significantly improves extrapolation during market trends.

- **Best Configuration:** The **E2 (LSTM + TCN)** ensemble paired with a **Random Forest meta-learner** yielded the best overall accuracy.
- **Performance Metrics (E2 + Random Forest):** 
  - **RMSE:** 0.009108 (in MinMax scaled space)
  - **$R^2$:** 0.98892
  - **MAPE:** 0.942%
- **Improvement:** This represents a ~49% reduction in RMSE relative to the best individual base model (CNN).
- **Meta-Learner Findings:** Interestingly, linear meta-learners (Ridge, Lasso) and tree ensembles (Random Forest, Extra Trees) outperformed complex gradient boosting models and neural networks when operating in the 2-dimensional delta space, avoiding overfitting. Feature scaling strategy (MinMax, Standard, Robust) had negligible impact on $R^2$, underscoring that the delta-transformation itself is the key driver of accuracy.

## Project Structure

```
.
├── .gitignore                      # Excludes temporary files, environments, and data caches
├── README.md                       # Project documentation (this file)
├── requirements.txt                # Python dependencies
├── data/                           
│   └── README.md                   # Dataset details and instructions to fetch
├── notebooks/                      
│   └── nifty50_forecasting.ipynb   # Main Jupyter notebook containing the experiments
└── results/                        
    └── model_comparison_e2.csv     # Model evaluation metrics from the paper
```

## Instructions to Run

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd nifty50-forecasting
   ```

2. **Set up a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Fetch the data:**
   See `data/README.md` for instructions, or simply run the dataset fetching cell provided within the notebook.

5. **Run the Notebook:**
   ```bash
   jupyter notebook notebooks/nifty50_forecasting.ipynb
   ```
   Execute the cells to train the base models (LSTM, CNN, TCN), perform the delta-transformation, train the 13 meta-learners, and view the comparison plots.
