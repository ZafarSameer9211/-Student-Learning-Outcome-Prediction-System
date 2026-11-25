# Student Learning Outcome Prediction System

## Project Overview
This project predicts student learning outcomes (PASS or FAIL) using machine learning techniques. It uses study hours, attendance, practice tests, sleep hours, and study methods to estimate student outcomes.

## Dataset
- Dataset: student_learning.csv
- Total Records: 280
- Target Variable: passed
- Classes: PASS (1) and FAIL (0)

## Machine Learning Models
- Dummy Classifier
- Logistic Regression
- Random Forest

## Best Model
Random Forest was selected based on its performance on the test dataset.

- Accuracy: 76.79%
- F1 Score: 0.7347

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## Project Features
- Data preprocessing
- Machine learning model training
- Model evaluation
- Saved model using Joblib
- Prediction for new student records
- Interactive Streamlit web application

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

## Responsible Use
This project is for educational demonstration only. Predictions must not be used to judge or penalize real students.
