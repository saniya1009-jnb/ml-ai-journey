import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + np.random.randn(100) * 2

# Plot it
plt.scatter(x, y, alpha=0.5)
plt.title("My first dataset")
plt.xlabel("x")
plt.ylabel("y")
plt.show()