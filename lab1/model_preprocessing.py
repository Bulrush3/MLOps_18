from sklearn.preprocessing import StandardScaler
import pandas as pd
import os

def preprocess_data(data):
    """Выполнение предобработки данных"""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.drop(columns=['Date', 'Location']))
    return scaled_data

if __name__ == "__main__":
    train_folder = "train"
    test_folder = "test"

    for folder in [train_folder, test_folder]:
        for file in os.listdir(folder):
            if file.endswith(".csv"):
                filepath = os.path.join(folder, file)
                data = pd.read_csv(filepath)
                preprocessed_data = preprocess_data(data)
                print(f"Preprocessed Data for {file}:")
                print(preprocessed_data)
