import random
import numpy as np
import matplotlib.pyplot as plt

def randmidpoint1D(nrc, sigma, seed):
    random.seed(seed)
    np.random.seed(seed)
    N = 2 * nrc
    x = np.zeros(N + 1)
    x[N] = sigma * np.random.randn()
    delta = [sigma * (0.5)**((i + 1) / 2) for i in range(nrc)]
    recursion(x, 0, N, 1, nrc, delta)
    return x

def recursion(x, t0, t2, t, nrc, delta):
    t1 = (t0 + t2) // 2
    x[t1] = 0.5 * (x[t0] + x[t2]) + delta[t] * np.random.randn()
    if t < nrc:
        recursion(x, t0, t1, t + 1, nrc, delta)
        recursion(x, t1, t2, t + 1, nrc, delta)

# Parameters
nrc = 6
sigma = 1
seed = -2

# Generate Brownian motion
x = randmidpoint1D(nrc, sigma, seed)

# Plot Brownian motion
plt.plot(x)
plt.title("Brownian Motion")
plt.xlabel("Steps")
plt.ylabel("Position")
plt.grid(True)
plt.show()
