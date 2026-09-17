# Diabetes Target Prediction Using Linear Regression

## 📌 Project Overview

This project implements a **Regression Machine Learning Model** for predicting a continuous target value from numerical input features.

The project uses the **Diabetes dataset** available through scikit-learn and applies Linear Regression with feature standardization.

---

## 🎯 Objectives

* Understand a regression dataset
* Separate features and target variables
* Split the dataset into training and testing sets
* Standardize numerical features
* Train a Linear Regression model
* Predict continuous target values
* Evaluate regression performance
* Compare actual and predicted values

---

## 📂 Dataset

The project uses the Diabetes regression dataset provided by scikit-learn.

The dataset contains numerical features related to patient measurements and a continuous target variable.

### Input

The model uses multiple numerical features as predictors.

### Output

The model predicts a **continuous target value**.

---

## 🤖 Machine Learning Algorithm

### Linear Regression

Linear Regression is a supervised machine-learning algorithm used to predict continuous numerical values.

The workflow used in this project is:

```text
Dataset
   ↓
Feature & Target Separation
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
Linear Regression
   ↓
Prediction
   ↓
Performance Evaluation
```

---

## 📊 Model Evaluation

The model is evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### Test Results

| Metric   |   Value |
| -------- | ------: |
| MAE      | 42.7941 |
| RMSE     | 53.8534 |
| R² Score |  0.4526 |

The results are based on the project's fixed train/test split (`random_state=42`).

---

## 📈 Actual vs Predicted

The project generates an **Actual vs Predicted** scatter plot.

Output:

```text
outputs/actual_vs_predicted.png
```

Points closer to the reference diagonal indicate predictions closer to the corresponding actual target values.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

---

## 📁 Project Structure

```text
Task-3-Regression-Model-for-Prediction/
│
├── data/
│   └── diabetes_regression.csv
│
├── notebook/
│   └── Task_3_Regression.ipynb
│
├── outputs/
│   ├── regression_metrics.csv
│   └── actual_vs_predicted.png
│
├── regression.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project

```bash
cd Task-3-Regression-Model-for-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the regression model

```bash
python regression.py
```

You can also open the Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
notebook/Task_3_Regression.ipynb
```

---

## 📋 Expected Output

The program displays:

```text
MAE: ...
RMSE: ...
R2 Score: ...
```

---

## ✅ Conclusion

This project demonstrates a complete regression workflow, from preparing the dataset and splitting the data to training a Linear Regression model and evaluating its predictions using standard regression metrics.

It provides a practical introduction to predicting continuous numerical outcomes using supervised machine learning.

---

## 👨‍💻 Author

**Allai**
B.Tech Artificial Intelligence and Data Science
