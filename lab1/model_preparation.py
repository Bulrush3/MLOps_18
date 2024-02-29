from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib
import os

def load_data_from_folder(folder):
    """Загрузка данных из папки"""
    dataframes = []
    label_encoder = LabelEncoder()
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            filepath = os.path.join(folder, file)
            data = pd.read_csv(filepath)
            data['Date'] = pd.to_datetime(data['Date']).dt.day
            data['Location'] = label_encoder.fit_transform(data['Location'])
            dataframes.append(data)
    return pd.concat(dataframes, ignore_index=True)

if __name__ == "__main__":
    # Загрузка данных из папки "train"
    train_data = load_data_from_folder("train")
    
    # Определение признаков и целевой переменной
    X_train = train_data.drop(columns=['Temperature'])
    y_train = train_data['Temperature']
    
    # Создание и обучение модели
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Сохранение обученной модели в файл
    joblib.dump(model, 'trained_model.pkl')

    # Оценка качества модели на обучающем наборе
    train_predictions = model.predict(X_train)
    train_mse = mean_squared_error(y_train, train_predictions)
    
    print("Training MSE:", train_mse)