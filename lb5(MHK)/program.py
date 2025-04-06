import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Дані
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([2.3, 3.0, 3.7, 4.5, 5.1, 5.7, 6.3, 7.1, 7.6])

# Лінійна регресія
a, b = np.polyfit(x, y, 1)  # a - коефіцієнт нахилу, b - зміщення

# Прогнозування
y_pred = a * x + b

# Помилка для коефіцієнта нахилу (a) та зміщення (b)
residuals = y - y_pred
n = len(x)  # кількість точок
S_xx = np.sum((x - np.mean(x)) ** 2)

# Стандартні помилки для a та b
stderr_a = np.sqrt(np.sum(residuals ** 2) / (n - 2)) / np.sqrt(S_xx)
stderr_b = np.sqrt(np.sum(residuals ** 2) / (n - 2)) * np.sqrt(np.mean(x ** 2) / S_xx)

# Коефіцієнт детермінації (R^2)
SS_total = np.sum((y - np.mean(y)) ** 2)
SS_residual = np.sum(residuals ** 2)
R_squared = 1 - (SS_residual / SS_total)

# F-статистика
MS_residual = SS_residual / (n - 2)
MS_model = SS_total / 1  # Для однієї моделі
F_statistic = MS_model / MS_residual

# Стандартна помилка для всієї регресії
S = np.sqrt(np.sum(residuals ** 2) / (n - 2))

# p-значення для F-статистики
p_value = 1 - stats.f.cdf(F_statistic, 1, n - 2)

# Виведення результатів
print(f'Коефіцієнт нахилу (a): {a:.4f}')
print(f'Помилка (коефіцієнта нахилу): {stderr_a:.4f}')
print(f'Коефіцієнт детермінації R^2: {R_squared:.4f}')
print(f'Помилка для залишків (S): {S:.4f}')
print(f'F-статистика: {F_statistic:.4f}')
print(f'Зміщення (b): {b:.4f}')
print(f'Помилка усунення: {stderr_b:.4f}')
print(f'Стандартна помилка для регресії: {S:.4f}')
print(f'Ступінь свободи: {n - 2}')
print(f'p-значення для F-статистики: {p_value:.4f}')

# Побудова графіка
plt.scatter(x, y, label='Дані')
plt.plot(x, y_pred, color='red', label=f'Регресія: y = {a:.2f}x + {b:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
