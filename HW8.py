import numpy as np
import matplotlib.pyplot as plt

print("Hit-or-Miss Monte Carlo Integration")


func_str = input("Enter the function: ")

def f(x):
    return eval(func_str, {"x": x, "np": np})


a = float(input("Enter a: "))
b = float(input("Enter b: "))
M = float(input("Enter vertical bound M: "))
n = int(input("Enter number n: "))


x = np.random.uniform(a, b, n)
y = np.random.uniform(0, M, n)


hits = y <= f(x)


area = (b - a) * M
integral_estimate = area * np.sum(hits) / n

print("Estimated integral:", integral_estimate)

x_vals = np.linspace(a, b, 1000)
plt.plot(x_vals, f(x_vals), color='black', label='f(x)')

plt.scatter(x[hits], y[hits], color='green', s=5, label='Hits (under curve)')
plt.scatter(x[~hits], y[~hits], color='red', s=5, label='Misses (above curve)')

plt.title("Hit-or-Miss Monte Carlo Integration")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()