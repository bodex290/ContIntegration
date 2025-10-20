# function.py
import numpy as np
import matplotlib.pyplot as plt

def add_numbers(a, b):
    return a + b

def generate_data(m=2.0, b=1.0, n=50, seed=0, noise=1.0):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, n)
    y = m * x + b + rng.normal(0, noise, size=n)
    return x, y

def fit_line(x, y):
    m, b = np.polyfit(x, y, 1)
    return float(m), float(b)

def plot_line(x, y, m, b, savepath=None, show=False):
    plt.figure()
    plt.scatter(x, y)
    plt.plot(x, m * x + b)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Best-fit line")
    if savepath:
        plt.savefig(savepath, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()

if __name__ == "__main__":
    # Optional manual run
    X, Y = generate_data()
    M, B = fit_line(X, Y)
    plot_line(X, Y, M, B, savepath="fit.png")