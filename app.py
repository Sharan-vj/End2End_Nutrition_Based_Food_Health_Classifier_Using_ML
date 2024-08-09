import pandas as pd
import joblib
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

model = joblib.load(filename='models/foodhealth_classifier.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    features = pd.DataFrame({
        'additives_n': [data['additives_n']],
        'fat_100g': [data['fat_100g']],
        'saturated-fat_100g': [data['saturated_fat_100g']],
        'carbohydrates_100g': [data['carbohydrates_100g']],
        'sugars_100g': [data['sugars_100g']],
        'fiber_100g': [data['fiber_100g']],
        'proteins_100g': [data['proteins_100g']],
        'sodium_100g': [data['sodium_100g']]
    })
    
    # Make prediction
    prediction = model.predict(features)
    prediction = int(prediction[0])

    if prediction == 0:
        message = "This food is not nutrient rich, It is not healthy to eat."
    else:
        message = "This food is nutrient rich, It is healthy to eat."

    # Return message as JSON
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
