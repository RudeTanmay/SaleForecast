from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the scaler, PCA, and model from files
with open('scaler.pkl', 'rb') as scaler_file:
    loaded_scaler = pickle.load(scaler_file)

with open('pca.pkl', 'rb') as pca_file:
    loaded_pca = pickle.load(pca_file)

with open('model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    store = int(request.form['store'])
    holiday_flag = int(request.form['holiday_flag'])
    temperature = float(request.form['temperature'])
    fuel_price = float(request.form['fuel_price'])
    cpi = float(request.form['cpi'])
    unemployment = float(request.form['unemployment'])
    weekday = int(request.form['weekday'])
    month = int(request.form['month'])
    year = int(request.form['year'])

    # Create a DataFrame from the input data
    input_df = pd.DataFrame({
        'Store': [store],
        'Holiday_Flag': [holiday_flag],
        'Temperature': [temperature],
        'Fuel_Price': [fuel_price],
        'CPI': [cpi],
        'Unemployment': [unemployment],
        'weekday': [weekday],
        'month': [month],
        'year': [year]
    })

    # Step 1: Standardize the input data using the fitted scaler
    input_df_scaled = loaded_scaler.transform(input_df)

    # Step 2: Transform the standardized data using the fitted PCA
    input_df_pca = loaded_pca.transform(input_df_scaled)

    # Step 3: Make a prediction using the pre-trained Random Forest model
    predicted_sales = loaded_model.predict(input_df_pca)[0]

    return render_template('result.html', predicted_sales=predicted_sales)

if __name__ == '__main__':
    app.run(debug=True)
