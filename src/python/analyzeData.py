import pandas as pd
df = pd.read_csv('student-study-performance\study_performance.csv')
head = df.head()


X = df.drop(columns=['math_score'],axis=1)
y = df['math_score']

num_features = X.select_dtypes(exclude="object").columns
cat_features = X.select_dtypes(include="object").columns


from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

numeric_transformer = StandardScaler()
oh_transformer = OneHotEncoder()

preprocessor = ColumnTransformer(
    [
        ("OneHotEncoder", oh_transformer, cat_features),
        ("StandardScaler", numeric_transformer, num_features),        
    ]
)

X = preprocessor.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True)

model = model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred[:5])

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.metrics import mean_squared_error, r2_score

import numpy as np

def evaluate_model(true, predicted):
    mae = mean_absolute_error(true, predicted)
    mse = mean_squared_error(true, predicted)
    rmse = np.sqrt(mean_squared_error(true, predicted))
    r2_square = r2_score(true, predicted)
    return mae, rmse, r2_square

mae, rmse, r2 = evaluate_model(y_test, y_pred)
print('Model performance for Training set')
print("- Root Mean Squared Error: {:.4f}".format(rmse))
print("- Mean Absolute Error: {:.4f}".format(mae))
print("- R2 Score: {:.4f}".format(r2))

import matplotlib.pyplot as plt

plt.scatter(y_test,y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

from joblib import dump
dump(model, '..\models\model.joblib')