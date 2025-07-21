# config.py

# ------------------------
# File Paths
# ------------------------

# Path to training dataset
DATA_PATH = "backend/data/employee_data.csv"

# Path to save/load trained model
MODEL_PATH = "backend/model/xgboost_model.pkl"

# ------------------------
# XGBoost Hyperparameters
# ------------------------

XGBOOST_PARAMS = {
    "n_estimators": 100,
    "max_depth": 4,
    "learning_rate": 0.1,
    "objective": "reg:squarederror",
    "random_state": 42
}

# ------------------------
# Flask App Settings
# ------------------------

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

# ------------------------
# Feature Columns
# ------------------------

CATEGORICAL_COLS = ["education_level", "job_role", "location"]
NUMERIC_COLS = ["years_of_experience"]
TARGET_COL = "salary"
