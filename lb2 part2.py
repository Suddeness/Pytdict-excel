import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

A = np.array([85, 92, 78, 81, 89, 85, 91, 77, 84, 88])
B = np.array([79, 82, 85, 88, 75, 83, 90, 80, 87, 84])
probabilities = np.array([0.1,0.2,0.5,0.3,0.4,0.6,0.7,0.8,0.10,0.9])

def calculate(data, prob):
    mean = np.mean(data)
    med = np.median(data)
    var = np.sum(np.multiply((data - mean)**2, prob))
    std = np.sqrt(var)
    return mean, med, var, std

def plot (val, prob, num=0):
    plt.bar(val, prob, color="pink")
    plt.xlabel("Випадкова величина")
    plt.ylabel("Ймовiрнiсть")
    plt.title("Модель")
    if num == 0:
        plt.savefig("main plot.png")
    else:
        plt.savefig("another plot.png")



mean, med, var, std = calculate(A, probabilities)
A_calc = [mean, med, var, std]
mean, med, var, std = calculate(B, probabilities)
B_calc = [mean, med, var, std]

print(f"A:\nСереднє значення: {A_calc[0]} \nМедіана: {A_calc[1]}  \nДисперсiя: {A_calc[2]} \nСтандартне вiдхилення: {A_calc[3]} \n")
print(f"B:\nСереднє значення: {B_calc[0]} \nМедіана: {B_calc[1]}  \nДисперсiя: {B_calc[2]} \nСтандартне вiдхилення: {B_calc[3]}\n")
plot(A, probabilities)
plot(B, probabilities, 1)

t_stat, p_value = stats.ttest_ind(A, B)
f_stat, p_value_var = stats.levene(A, B)

print(f"t-тест:\nt-статистика: {t_stat}\np-значеня: {p_value}\n")
print(f"F-тест (дисперсія):\nF-статистика: {f_stat}\np-значеня: {p_value_var}")
