import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor

# Load dataset
data_path = "../data/employee_data.csv"
df = pd.read_csv(data_path)

# Example columns — adjust to your actual dataset
categorical_features = ['education_level', 'job_role', 'location']
numerical_features = ['years_of_experience']

target_column = 'salary'

# Split features and target
X = df[categorical_features + numerical_features]
y = df[target_column]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
    ],
    remainder='passthrough'  # Keep numerical features
)

# XGBoost model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6,
        random_state=42
    ))
])

# Train the model
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print(f"Model trained. RMSE: {rmse:.2f}, R²: {r2:.2f}")

# Save model
model_output_path = "xgboost_model.pkl"
joblib.dump(model, model_output_path)
print(f"Model saved to: {model_output_path}")
