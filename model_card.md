# Model Card: Student Learning Outcome Prediction System

## 1. Model Details
- Model Name: Random Forest Classifier
- Model Type: Supervised Machine Learning
- Task: Binary Classification
- Framework: Scikit-learn
- Model File: student_model.joblib

## 2. Intended Use
The model predicts student learning outcomes as PASS or FAIL based on study-related features.

It is designed for educational demonstration and beginner machine learning practice.

## 3. Dataset Information
- Dataset Name: student_learning.csv
- Total Records: 280
- Training Samples: 224
- Testing Samples: 56
- Target Variable: passed
- Dataset Type: Synthetic

## 4. Input Features
- hours_studied
- attendance
- practice_tests
- sleep_hours
- study_method

The final_score feature was excluded to prevent data leakage.

## 5. Model Performance

| Metric | Value |
|---|---|
| Accuracy | 76.79% |
| F1 Score | 0.7347 |
| Test Samples | 56 |

## 6. Limitations
- The dataset is relatively small.
- The dataset contains synthetic information.
- Predictions may be incorrect.
- Model performance may not generalize to real students.
- Predicted probabilities are estimates, not guarantees.

## 7. Ethical Considerations
This model must not be used to judge, penalize, rank, or make important academic decisions about real students.

## 8. Conclusion
The project demonstrates a complete machine learning workflow, including data preprocessing, model training, evaluation, model saving, and Streamlit deployment.
