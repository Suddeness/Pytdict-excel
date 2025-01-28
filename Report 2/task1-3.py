import numpy as np
import time
def simple_variant(a,b,x0,tol=1e-6,max_iter=100):
       #start = time.time()
       n = len(b)
       x = x0.copy()
       for iteration in range(max_iter):
           x_new = np.zeros_like(x)
           for i in range(n):
               if i == 0:
                   sum_ax = sum(a[i][j] * x[j] for j in range(n) if j != i)
                   x_new[i] = (b[i] - sum_ax) / a[i][i]
               else:
                   x_new[i] = (b[i] - x_new[i-1]) / a[i][i]
           if np.linalg.norm(x_new - x, ord=np.inf) < tol:
               #print(f"time:{time.time() - start}")
               return x_new, iteration + 1, float(np.linalg.norm(x_new - x, ord=np.inf))
           x = x_new
       return x, max_iter

def seidel_iteration(a, b, x0, tol=1e-6, max_iter=100):
    #start = time.time()
    n = len(b)
    x = x0.copy()
    for iteration in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            mr_i = sum(a[i][j] * x_new[j] for j in range(i + 1, n))
            sum_ax = sum(a[i][j] * x_new[j] for j in range(i)) + mr_i
            x_new[i] = (b[i] - sum_ax) / a[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            #print(f"time:{time.time() - start}")
            return x_new, iteration + 1, float(np.linalg.norm(x_new - x, ord=np.inf))
        x = x_new
    return x, max_iter

#3x-y=7   x+2y=4
a = np.array([[3,-1],[1,2]],dtype=float)
b = np.array([7,4],dtype=float)
x0 = np.zeros_like(b,dtype=float)

x, iterat, tl = simple_variant(a,b,x0)
print(f"програмна реалізація\nрезультат {x}, з точністю {tl:.6f} за {iterat} ітерацій")
#start=time.time()
result = np.linalg.solve(a, b)
print(f"\nпакетна реалізація\n результат {result}")
#print(f"time:{time.time() - start}")
