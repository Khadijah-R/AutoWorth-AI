# 🚗 AutoWorth AI — Used Car Price Prediction

**An end-to-end Machine Learning project that estimates used car market prices and evaluates whether a seller's asking price represents a good deal.**

🔗 **Live Demo:** [Try AutoWorth AI](https://autoworth-ai-1.streamlit.app/)

## 📌 Project Overview

AutoWorth AI is a machine learning web application developed as a final project for the AI course at Alexandria Training Center – WE.

The application predicts a used car's estimated market price based on its characteristics and compares that estimate with the seller's asking price to provide a simple deal assessment.

## ✨ Key Features

- **Used Car Price Prediction:** Estimates a car's market value from its specifications.
- **Deal Assessment:** Compares the estimated value with the seller's asking price.
- **Interactive Web Interface:** Enter vehicle details and receive a prediction.
- **Machine Learning Pipeline:** Uses a trained model and preprocessing pipeline.
- **Visual Comparison:** Displays the estimated price alongside the asking price.

## 🧠 Machine Learning

- **Model:** Random Forest Regression
- **Data Processing:** Feature preprocessing and feature engineering
- **Evaluation:** R², Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE)

### Previously Recorded Evaluation Results

The following results were previously recorded from the model evaluation notebook and should be rechecked against the final saved notebook before being treated as verified:

| Metric | Result |
|---|---:|
| R² | 0.9443 |
| MAE | £1,353.97 |
| RMSE | £2,336.66 |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## 🚀 Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Khadijah-R/AutoWorth-AI.git
   cd AutoWorth-AI
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

The application downloads the trained model artifacts from the project's GitHub Release when needed.

## 📂 Project Structure

```text
AutoWorth-AI/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── AutoWorth_AI_Enhanced.ipynb
```

## 🎯 Project Goal

This project demonstrates how machine learning can be applied to a real-world pricing problem through model development, evaluation, deployment, and an interactive web application.

## 👩‍💻 Author

**Khadijah Raed Abdelrahman Abouelhossien**

[GitHub Repository](https://github.com/Khadijah-R/AutoWorth-AI) · [Live Application](https://autoworth-ai-1.streamlit.app/)
