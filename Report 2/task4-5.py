import numpy as np
# Матрица
A = np.array([[3, -1],
              [1,  2]])
B = np.array([7, 4])
X = np.linalg.solve(A, B)

#4.1
cond_A = np.linalg.cond(A)
print(f"міра обумовленості A: {cond_A:.2f}\n")

#4.2
B_n = B * 1.01 #шум
X_n = np.linalg.solve(A, B_n)
Err = np.linalg.norm(X_n - X)/ np.linalg.norm(X)
print(f"відносна похибка: {Err:.5f}\n")
print(f"без шуму: {X}\nз шумом: {X_n}\n")

#5
if Err < 0.1:
    print("Система стійка.")
else:
    print("Система нестійка.")
