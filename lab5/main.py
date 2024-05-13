import pandas as pd
import numpy as np

def generate_data(n_obs=500, noise=False):
    # Генерация данных
    gender = pd.Categorical(np.random.randint(0, 2, size=n_obs))
    age = np.random.randint(17, 25, size=n_obs)
    hours_studied = np.random.randint(1, 10, size=n_obs)
    extracurricular_activities = pd.Categorical(np.random.randint(0, 2, size=n_obs)).astype(int)
    exam_score = 10 * hours_studied + 5 * extracurricular_activities + 5 * np.random.randn(n_obs)

    # Создание датафрейма
    data = pd.DataFrame({
        "пол": gender,
        "возраст": age,
        "часы_учебы": hours_studied,
        "внеучебные_занятия": extracurricular_activities,
        "баллы_за_экзамен": exam_score
    })

    # Добавление шума
    if noise:
        data["баллы_за_экзамен"] = data["баллы_за_экзамен"] + 10 * np.random.randn(n_obs)

    return data

# Пример использования
student_data = generate_data(n_obs=1000, noise=True)
print(student_data.head())

df_1 = generate_data()
df_2 = generate_data()
df_3 = generate_data()
df_4 = generate_data(noise=True)

df_1.to_csv("df_1/df.сsv", index=False)
df_2.to_csv("df_2/df.сsv", index=False)
df_3.to_csv("df_3/df.сsv", index=False)
df_4.to_csv("df_4/df.сsv", index=False)