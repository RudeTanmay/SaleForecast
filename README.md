
# Walmart Sales Prediction

## Project Description

This project aims to predict the weekly sales for Walmart stores based on various factors, including store number, holiday flag, temperature, fuel price, CPI (Consumer Price Index), unemployment rate, and more. By leveraging machine learning techniques, we can help optimize inventory management, marketing strategies, and operational efficiency for Walmart.

The dataset used for this project can be found at the following link: [Walmart Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/walmart-dataset).

## Features

- Predict weekly sales based on multiple input parameters.
- User-friendly web interface for inputting data.
- Real-time predictions with clear results displayed to the user.

## Technologies Used

- Python
- Flask
- scikit-learn
- HTML/CSS
- Pandas
- NumPy

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment named `wsp`:

```bash
python -m venv wsp
```

- **Windows**:
  ```bash
  wsp\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source wsp/bin/activate
  ```

### 3. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Once the environment is set up and dependencies are installed, run the application:

```bash
python app.py
```

### 5. Access the Application

Open your web browser and navigate to `http://127.0.0.1:5000/` to access the Walmart Weekly Sales Prediction application.

## Usage

1. Enter the required input parameters in the form fields.
2. Click the "Predict Sales" button to submit the form.
3. View the predicted sales displayed on the result page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Kaggle](https://www.kaggle.com/) for providing the dataset.
- The open-source community for the tools and libraries used in this project.
