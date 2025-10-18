# Applied AI Portfolio — Tecnológico de Monterrey

**Author:** Carlos F. del Castillo Rey  
**Program:** Master’s in Applied Artificial Intelligence  

This repository contains academic projects demonstrating the application of **Machine Learning, Data Science, and Artificial Intelligence** techniques in real-world contexts such as predictive modeling, time-series forecasting, classification, and recommendation systems.  
All notebooks were developed as part of the **course “Inteligencia Artificial y Aprendizaje Automático” (AI & Machine Learning)**.

---

## Overview

| # | Notebook Name | Description |
|---|----------------|-------------|
| 1 | **Linear-Regression_California-Housing.ipynb** | Implements a full regression workflow using the California Housing dataset. Includes EDA, feature transformations (Box-Cox, log, square-root), and custom metric implementation (RMSE, MAE, MAPE) with K-Fold validation. |
| 2 | **Employee-Attrition_Prediction-IBM-HR.ipynb** | Predictive analytics model for employee attrition using logistic regression and KNN. Covers data cleaning, encoding, stratified splitting, hyperparameter tuning, and performance evaluation. |
| 3 | **Credit-Risk_Prediction_SouthGermanDataset.ipynb** | Classification model for credit scoring using the South German Credit dataset. Includes feature engineering, class rebalancing (SMOTE), and evaluation across multiple algorithms (RF, KNN, XGBoost, MLP). |
| 4 | **Learning-Curves_Facebook-Ads.ipynb** | Regression models to predict social media engagement based on Facebook campaign metrics. Demonstrates cyclical variable encoding, feature engineering, and learning curve analysis to diagnose overfitting and underfitting. |
| 5 | **Imbalanced-Classification_Oil-Spill.ipynb** | Binary classification of oil spill occurrences from satellite images. Uses geometric mean (G-Mean), ROC, and Precision-Recall curves for imbalanced evaluation and model benchmarking. |
| 6 | **Time-Series-Forecasting_Champagne-Sales.ipynb** | Forecasting project comparing ARIMA, Prophet, and LSTM models on monthly champagne sales data. Evaluates performance via RMSE and visual comparison of model predictions. |
| 7 | **Recommendation-System_SVD_Restaurant-Ratings.ipynb** | Recommender system built with Singular Value Decomposition (SVD) using the UCI Restaurant & Consumer dataset. Demonstrates matrix construction, cleaning, and cosine similarity for item recommendations. |
| 8 | **Forecasting_Prophet-LSTM-ARIMA.ipynb** | Advanced comparison of hybrid time-series models (ARIMA, Prophet, LSTM). Focuses on scaling, sequence generation, and deep learning evaluation for trend forecasting. |
| 9 | **Multimodel-Learning_Evaluation.ipynb** | Multi-algorithm comparison on regression and classification problems using cross-validation and model interpretability techniques. |
| 10 | **Dimensionality-Reduction_SVD.ipynb** | Practical demonstration of dimensionality reduction using TruncatedSVD for feature compression and latent structure discovery in user-item matrices. |
| 11 | **Social-Media-Performance_Modeling.ipynb** | Modeling of post-performance metrics on Facebook using supervised regression and feature importance analysis from Moro et al. (Elsevier). |
| 12 | **Regression-Modeling_with-FeatureEngineering.ipynb** | Exploratory regression notebook focusing on transformation pipelines, scaling, and feature selection to optimize prediction accuracy. |
| 13 | **Predictive-Analytics_Pipeline-EDA.ipynb** | Comprehensive pipeline integrating preprocessing, encoding, and model evaluation using scikit-learn’s modular approach. |

---

## Technologies Used

- **Languages:** Python 3.10+, SQL (for data extraction)
- **Libraries:** scikit-learn, pandas, numpy, seaborn, matplotlib, TensorFlow/Keras, Prophet, XGBoost, imbalanced-learn
- **Concepts:**  
  - Supervised Learning (Regression, Classification)  
  - Model Evaluation (Cross-validation, Learning Curves, ROC/PR)  
  - Dimensionality Reduction (SVD)  
  - Time-Series Forecasting (ARIMA, Prophet, LSTM)  
  - Recommender Systems  
  - Data Preprocessing & Feature Engineering  

---

## Repository Structure
```
Applied-AI-Portfolio_TecMonterrey/
│
├── Linear-Regression_California-Housing.ipynb
├── Employee-Attrition_Prediction-IBM-HR.ipynb
├── Credit-Risk_Prediction_SouthGermanDataset.ipynb
├── Learning-Curves_Facebook-Ads.ipynb
├── Imbalanced-Classification_Oil-Spill.ipynb
├── Time-Series-Forecasting_Champagne-Sales.ipynb
├── Recommendation-System_SVD_Restaurant-Ratings.ipynb
├── (other notebooks...)
└── README.md
```

---

## Keywords / Tags
machine-learning, data-science, artificial-intelligence, regression, classification, forecasting, recommendation-systems, time-series, svd, prophet, lstm, scikit-learn, python, applied-ai, tec-de-monterrey
