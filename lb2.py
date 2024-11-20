import numpy as np
import random
from scipy.stats import t, chi2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

own_data = []
for _ in range(1,11):
    own_data.append(random.randint(1,30))

def main_char (data):
    mean = np.mean(data)
    med = np.median(data)
    var = np.var(data, ddof=1)
    return mean, med, var

def coffin_mean(data, confidence=0.95):
    n = len(data)
    mean, _, variance = main_char(data)
    t_value = t.ppf((1 + confidence) / 2, n - 1)
    margin_of_error = t_value * (np.sqrt(variance) / np.sqrt(n))
    return mean - margin_of_error, mean + margin_of_error

def coffin_variance(data, confidence=0.95):
    n = len(data)
    _, _, variance = main_char(data)
    chi2_lower = chi2.ppf((1 - confidence) / 2, n - 1)
    chi2_upper = chi2.ppf((1 + confidence) / 2, n - 1)
    lower_bound = (n - 1) * variance / chi2_upper
    upper_bound = (n - 1) * variance / chi2_lower
    return lower_bound, upper_bound

def plot(data, bins=10):
    plt.hist(data, bins=bins, color='purple', edgecolor='black')
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.title('Гістограма вибірки')
    plt.savefig("plot.png")


mean = coffin_mean(own_data)
var = coffin_variance(own_data)
convert_mean = tuple(el.item() for el in mean)
convert_var = tuple(el.item() for el in var)

print("Середнє значення:", np.mean(own_data))
print(f"Довірчий інтервал для середнього: {convert_mean[0]}, {convert_mean[1]}")
print(f"Довірчий інтервал для дисперсії: {convert_var[0]}, {convert_var[1]}" )
plot(own_data)
