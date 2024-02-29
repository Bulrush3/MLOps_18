import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import joblib

# Загрузка тестовых данных из файла CSV
test_data = pd.read_csv("test/london_test.csv")
label_encoder = LabelEncoder()
test_data['Date'] = pd.to_datetime(test_data['Date']).dt.day
test_data['Location'] = label_encoder.fit_transform(test_data['Location'])

# Определение признаков и целевой переменной для тестового набора
X_test = test_data.drop(columns=['Temperature'])
y_test = test_data['Temperature']

# Загрузка обученной модели из файла
model = joblib.load("trained_model.pkl")

# Предсказание температуры на тестовом наборе данных
test_predictions = model.predict(X_test)

# Оценка качества модели на тестовом наборе
test_mse = mean_squared_error(y_test, test_predictions)

print("Test MSE:", test_mse)