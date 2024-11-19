import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x_values = np.array([1,2,3,4,5])
probabilities = np.array([0.1,0.2,0.5,0.3,0.4])
E_X = np.sum(x_values * probabilities)
Var_X = np.sum(np.multiply((x_values-E_X)**2, probabilities))
Std_X = np.sqrt(Var_X)
print(f"Математичне сподiвання: {E_X} \nДисперсiя: {Var_X} \nСтандартне вiдхилення: {Std_X}")

def plot (val, prob):
    plt.bar(val, prob, color="pink")
    plt.xlabel("Випадкова величина")
    plt.ylabel("Ймовiрнiсть")
    plt.title("Модель дискретної випадкової величини")
    plt.savefig("plot.png")
plot(x_values, probabilities)