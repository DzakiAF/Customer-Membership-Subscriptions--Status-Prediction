# Customer Subscription Status Prediction

## 📌 Project Overview
This project aims to predict whether a customer will subscribe to a service based on various attributes. The goal is to build a classification model that provides accurate predictions to enhance customer retention and marketing strategies.

## 📂 Dataset
- **Description**: The dataset contains customer-related features along with their subscription status (subscribed or not).
- **Main Features**:
  - `customer_id`: Unique identifier for each customer.
  - `age`: Customer's age.
  - `gender`: Male/Female.
  - `region`: Customer's location.
  - `purchase_history`: Previous transactions.
  - `subscription_status`: Target variable (0 = Not Subscribed, 1 = Subscribed).

## 🔧 Tech Stack
- **Python**
- **Pandas & NumPy** (Data Processing)
- **Scikit-learn** (Machine Learning)
- **Matplotlib & Seaborn** (Visualization)
- **XGBoost** (Boosting Algorithm)

## 📌 Workflow
1. **Data Preprocessing**
   - Handling missing values
   - Encoding categorical variables
   - Feature scaling
2. **Model Training & Evaluation**
   - Algorithms used: `KNN`, `SVM`, `Decision Tree`, `Random Forest`, `XGBoost`
   - Evaluation Metrics: Accuracy, Precision, Recall, F1-Score
3. **Best Model Selection**
   - The best model was **Decision Tree** with an **F1-Score of 0.759**.

## 📊 Results
- **Accuracy**: [Provide Accuracy Score]
- **F1-Score**: 0.759
- **Best Model**: Decision Tree

## 🤝 Contribution
If you would like to contribute, please **fork** this repository and submit a **pull request** with your proposed changes!

---
✨ **Created by DzakiAF**

