# Results: Visualizations

This file outlines the key visual figures from the study. 

> [!NOTE]
> To view the actual images in this repository, please export the graphs from the Colab notebook and save them in the `images/` directory at the root of the project with the corresponding filenames below.

## Figure 1: Proposed Architecture
**File:** `../images/architecture.png`
*Description:* A flowchart detailing the two-layer stacked ensemble architecture. It shows the input window feeding into the base models (LSTM and CNN/TCN). Their outputs and the target are transformed into delta space, which is then fed to the Meta-Learner to produce the final predicted change.

## Figure 2: 5-Fold Cross-Validation Robustness
**File:** `../images/cv_rmse_bar_chart.png`
*Description:* Bar charts displaying the 5-fold cross-validation RMSE (mean $\pm$ std) per meta-learner for both E1 (LSTM+CNN) and E2 (LSTM+TCN) configurations in delta-space. It highlights the stability and tight variance of the linear and tree-based meta-learners.

## Figure 3: Base Learner Predictions (Test Set)
**File:** `../images/base_learners_predictions.png`
*Description:* Three line graphs comparing the actual scaled closing price vs. the predicted closing price for each individual base learner (LSTM, CNN, and TCN) on the test set. Shows the systematic lag present in the individual sequence models during the 2023 sustained market rally.

## Figure 4: Final Ensemble Predictions (E2 + RandomForest)
**File:** `../images/best_ensemble_predictions.png`
*Description:* A line graph comparing the actual scaled closing price against the predictions of our best configuration: E2 (LSTM+TCN) with a RandomForest meta-learner. Visually demonstrates the power of the delta-space correction, as the predicted series tightly tracks the actual index through both consolidation phases (2022) and extended uptrends (late 2023) without the systematic lag seen in Figure 3.
