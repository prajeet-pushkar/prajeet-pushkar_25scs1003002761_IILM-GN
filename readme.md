# 🌾 Crop Recommendation System

A Machine Learning–based **Crop Recommendation System** that suggests the most suitable crop to grow based on soil nutrients and environmental conditions.  
The project uses a Random Forest Classifier trained on the *Crop_recommendation.csv* dataset and is deployed as a simple **Flask web app**.

---

## 📌 Features

- Predicts the **best crop** to grow using:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature (°C)
  - Humidity (%)
  - pH value
  - Rainfall (mm)
- Simple and clean **web interface** for user input.
- Backend built with **Flask** and **scikit-learn**.
- Trained on a real-world agricultural dataset.

---

## 🧠 Tech Stack

- **Programming Language:** Python  
- **Backend Framework:** Flask  
- **ML Library:** scikit-learn  
- **Data Handling:** pandas, numpy  
- **Visualization (Notebook):** matplotlib, seaborn  
- **Frontend:** HTML, CSS (basic)

---

## 📊 Dataset

- File: `Crop_recommendation.csv`  
- Columns:
  - `N`, `P`, `K` – Soil macronutrients
  - `temperature`
  - `humidity`
  - `ph`
  - `rainfall`
  - `label` – Target crop (rice, wheat, maize, etc.)

The model is trained using a **RandomForestClassifier** with an 80/20 train–test split.

---

## 📂 Project Structure

```text
Crop Prediction/
│
├── app.py                      # Flask app (backend + model)
├── Crop_recommendation.csv     # Dataset
├── crop recommendation.ipynb   # Jupyter notebook (EDA + training)
│
└── templates/
    ├── index.html              # Input form page
    └── result.html             # Prediction result page
