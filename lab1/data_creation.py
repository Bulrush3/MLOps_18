import pandas as pd
import numpy as np
import os

def generate_temperature_data(location, start_date, end_date, noise_level=0.5):
    """Генерация данных о температуре для заданной локации"""
    dates = pd.date_range(start=start_date, end=end_date)
    temperatures = np.random.normal(loc=20, scale=5, size=len(dates))
    temperatures += np.random.normal(scale=noise_level, size=len(dates))
    data = pd.DataFrame({'Date': dates, 'Temperature': temperatures})
    data['Location'] = location
    return data

def save_dataset(data, directory, filename):
    """Сохранение набора данных в CSV файл"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    data.to_csv(filepath, index=False)
    print(f"Dataset saved to {filepath}")

if __name__ == "__main__":
    # Генерация данных для Москвы
    moscow_data = generate_temperature_data('Moscow', '2024-01-01', '2024-01-31', noise_level=2)
    save_dataset(moscow_data, 'train', 'moscow_train.csv')
    
    # Генерация данных для Нью-Йорка
    newyork_data = generate_temperature_data('New York', '2024-01-01', '2024-01-31', noise_level=3)
    save_dataset(newyork_data, 'train', 'newyork_train.csv')
    
    # Генерация данных для Лондона
    london_data = generate_temperature_data('London', '2024-01-01', '2024-01-31', noise_level=1)
    save_dataset(london_data, 'test', 'london_test.csv')