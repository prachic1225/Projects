**Weather Forecasting**
A beginner-level time-series forecasting project that predicts hourly temperature at Jena, Germany from its own recent history (lag features) plus calendar features, benchmarked against naive and seasonal-naive baselines.

**Problem Statement**
Given an hourly temperature series, forecast the next value. The key question for any forecaster: does it beat the seasonal-naive baseline (same hour yesterday)? We use a chronological train/test split (never shuffle time) and score MAE / RMSE / MAPE / R².

**Dataset**
Source: Jena Climate (Max Planck Institute, via TF-Keras)
Series: 10-minute records resampled to hourly, years 2015–2016 → 17,471 hours.
Target: temperature (°C); also carries pressure and humidity.
Dataset note: the checklist's Kaggle historical-hourly-weather set is replaced by the openly hosted Jena Climate dataset (a standard weather-forecasting benchmark).

**Features & Models**
Features: lags (1, 2, 3, 24, 48, 168 h), rolling mean/std (24 h, 168 h), calendar (hour, day, month, day-of-week, weekend).
Models: naive + seasonal-naive baselines vs Linear, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting, KNN.

**Key Findings**
Next-hour temperature is highly forecastable — Linear Regression reaches MAE 0.39 °C (R² 0.995), because temperature is smooth and strongly autocorrelated at lag 1.
ML crushes the baselines — RMSE 0.57 vs seasonal-naive 3.06 (5×) and naive 13.9 (24×): lag + calendar features capture both the daily cycle and the slow trend.
A linear model wins — with informative lag features the relationship is near-linear, so Linear/Ridge edge out the tree ensembles (and run far faster).
The lag-1 feature does most of the work — temperature changes little hour-to-hour; the value of the model is in the multi-hour and daily-cycle features that refine that persistence.
