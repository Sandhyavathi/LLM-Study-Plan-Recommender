from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('study_plan_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prompt = data['prompt']
    
    # Vectorize the input prompt
    prompt_vectorized = vectorizer.transform([prompt])
    
    # Make prediction
    prediction = model.predict(prompt_vectorized)
    
    return jsonify({'predicted_study_plan': prediction[0]})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT env variable
    app.run(host='0.0.0.0', port=port, debug=False)  # Debug should be off in production
