import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import chardet, xlsxwriter
import seaborn as sns

#1. Завантаження та попередня обробка даних
def one():
    data = pd.read_csv("Mobiles Dataset (2025).csv", encoding="latin1") # Завантаження даних
    # Ознайомлення з даними
    print(f"data head:\n{data.head()}\n")
    print(f"datainfo: \n{data.info()}\n")

    # Перевірка та заповнення пропущених значень середнім якщо е:
    data.replace(["", "NaN", "none", "null", 0], np.nan, inplace=True)
    data_null = data.isnull().sum()
    for col, val in data_null.items():
        if val > 0:
            print(f"{col} - {val}")
            data[col].fillna(data[col].mean(), inplace=True)
    return data
#2. Аналіз статистичних характеристик вибірки. Обчислення статистичних показників:

def clean_numeric_string(value): #функція для очищення рядків
    if isinstance(value, str):
        value = ''.join(c for c in value if c.isdigit() or c == '.')
        return pd.to_numeric(value, errors='coerce')
    return value

def two (data):
    ret_data = {'Показник': ['Середнє значення', 'Медіана', 'Мода', 'Дисперсія', 'Стандартне відхилення']}
    usch = int(input("enter column quantity: "))
    for e, (col, val) in enumerate(data.items()):
        if e >= usch:
            break
        data[col] = data[col].apply(lambda x: clean_numeric_string(x))
        if data[col].notna().any():
            mean_value = data[col].mean()  # Середнє значення
            median_value = data[col].median()  # Медіана
            mode_value = data[col].mode()[0] # Мода
            variance_value = data[col].var()  # Дисперсія
            std_deviation = data[col].std()  # Стандартне відхилення
            print(f"for column {col}:\n mean = {mean_value}, median = {median_value}, Мода: {mode_value},"
                  f"\nvariance = {variance_value}, std = {std_deviation}\n")
            ret_data[col] = [mean_value, median_value, mode_value, variance_value, std_deviation]
        else:
            print(f"for column {col}:\nall elements is none\n")
            ret_data[col] = [None,None,None,None,None,]
    return ret_data

#3. Візуалізація даних. Побудова гістограми:
def three(data):
    plt.figure(figsize=(10,6))
    sns.histplot(data["Launched Year"], bins=30, kde=True)
    plt.title('Гістограма розподілу параметра')
    plt.xlabel('Значення параметра')
    plt.ylabel('Частота')
    plt.savefig("1.png")
    plt.close()
    #Побудова діаграми розсіювання:
    plt.figure(figsize=(20,15))
    sns.scatterplot(x=data['Launched Price (Pakistan)'], y=data['Launched Price (India)'])
    plt.title('Діаграма розсіювання параметрів')
    plt.xlabel('Параметр X')
    plt.ylabel('Параметр Y')
    plt.xticks(fontsize=8, rotation=45)
    plt.yticks(fontsize=8)
    plt.savefig("2.png")
    plt.close()

#4. Побудова довірчих інтервалів. Обчислення довірчого інтервалу для середнього:
def four(data):
    col = "RAM"
    data[col] = data[col].apply(lambda x: clean_numeric_string(x))
    sample = data[col]  # Вибірка параметра
    n = len(sample)  # Розмір вибірки
    confidence = 0.95  # Рівень довіри
    mean = np.mean(sample)  # Середнє
    sem = stats.sem(sample)  # Стандартна помилка

    # Визначення довірчого інтервалу для t-розподілу
    h = sem * stats.t.ppf((1 + confidence) / 2, n - 1)
    lower_bound = mean - h
    upper_bound = mean + h
    print("Довірчий інтервал:", (lower_bound, upper_bound))

#5. Експорт результатів в Excel. Збереження статистичних показників:
def five():
    data = one()
    results = pd.DataFrame(two(data))
    three(data)# Створення DataFrame з результатами
    four(data)
    image1="1.png"
    image2="2.png"
    with pd.ExcelWriter('results.xlsx',engine='xlsxwriter') as file:
        results.to_excel(file,sheet_name="stats", index=False)
        workbook = file.book
        worksheet = file.sheets['stats']
        worksheet.insert_image('E2', image1, {'x_scale': 0.5, 'y_scale': 0.5})
        worksheet.insert_image('E10', image2, {'x_scale': 0.5, 'y_scale': 0.5})
five()
