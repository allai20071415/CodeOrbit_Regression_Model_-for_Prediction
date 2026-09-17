import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("data/diabetes_regression.csv")
X = df.drop(columns=["target"])
y = df["target"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = Pipeline([("scaler",StandardScaler()),("regressor",LinearRegression())])
model.fit(X_train,y_train)
pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test,pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test,pred)))
print("R2 Score:", r2_score(y_test,pred))
