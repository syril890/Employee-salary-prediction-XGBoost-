from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

# Initialize the app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Load the trained model
model = joblib.load('model/xgboost_model.pkl')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict_salary():
    try:
        data = request.get_json()

        # Example expected input: adjust according to your real model
        # {
        #   "education_level": "Master's",
        #   "years_of_experience": 5,
        #   "job_role": "Data Scientist",
        #   "location": "Bangalore"
        # }

        # You may need preprocessing based on how the model was trained
        df = pd.DataFrame([data])

        # If you have custom preprocessing logic, apply it here
        # from utils.preprocessing import preprocess_input
        # df = preprocess_input(df)

        prediction = model.predict(df)

        return jsonify({
            'predicted_salary': round(prediction[0], 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Health check route
@app.route('/', methods=['GET'])
def home():
    return "XGBoost Employee Salary Predictor is running."

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
