from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load and train model
crop = pd.read_csv("Crop_recommendation.csv")
X = crop.drop('label', axis=1)
y = crop['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    N = int(request.form['N'])
    P = int(request.form['P'])
    K = int(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])
    
    # Minimum valid values based on dataset
    MIN_N = 0.0
    MIN_P = 5.0
    MIN_K = 5.0
    MIN_TEMPERATURE = 8.825675
    MIN_HUMIDITY = 14.258040
    MIN_PH = 3.504752
    MIN_RAINFALL = 20.211267
    # Validation
    if (N < MIN_N or P < MIN_P or K < MIN_K or temperature < MIN_TEMPERATURE or 
    humidity < MIN_HUMIDITY or ph < MIN_PH or rainfall < MIN_RAINFALL):
        error_message = (
        "❌ The entered values are too low and do not match realistic agricultural conditions. "
        "Please enter valid values above the minimum range."
    )
        return render_template("index.html", error=error_message)


    
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    result = prediction[0]
    
    return render_template('result.html', crop=result)

if __name__ == '__main__':
    app.run(debug=True)
