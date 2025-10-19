import os
import shutil

base = r"D:\Mestria\ML\Github"

folders = {
    "01_Regression": [
        "Linear-Regression_California-Housing.ipynb",
        "Regression-Modeling_with-FeatureEngineering.ipynb",
    ],
    "02_Classification": [
        "Employee-Attrition_Prediction-IBM-HR.ipynb",
        "Credit-Risk_Prediction_SouthGermanDataset.ipynb",
        "Imbalanced-Classification_Oil-Spill.ipynb",
    ],
    "03_TimeSeries": [
        "Time-Series-Forecasting_Champagne-Sales.ipynb",
        "Forecasting_Prophet-LSTM-ARIMA.ipynb",
    ],
    "04_Recommenders": [
        "Recommendation-System_SVD_Restaurant-Ratings.ipynb",
        "Predictive-Analytics_Pipeline-EDA.ipynb",
    ],
    "05_Multimodel": [
        "Learning-Curves_Facebook-Ads.ipynb",
        "Multimodel-Learning_Evaluation.ipynb",
        "Dimensionality-Reduction_SVD.ipynb",
    ],
    "06_NLP": [],       # Espacio reservado para tus notebooks de procesamiento de lenguaje natural
    "07_BigData": []    # Espacio reservado para notebooks de PySpark / MLlib / sistemas distribuidos
}

for folder, files in folders.items():
    dest_folder = os.path.join(base, folder)
    os.makedirs(dest_folder, exist_ok=True)
    for f in files:
        src = os.path.join(base, f)
        dest = os.path.join(dest_folder, f)
        if os.path.exists(src):
            shutil.move(src, dest)
            print(f"✅ Moved: {f} → {folder}")
        else:
            if f:
                print(f"⚠️ File not found: {f}")

print("\n🎯 Portfolio structure created successfully with NLP & Big Data folders.")
