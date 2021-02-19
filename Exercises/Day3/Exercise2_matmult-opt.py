import numpy as np

N = 250
X = np.random.randint(100, size=(N, N))
Y = np.random.randint(100, size=(N, N + 1))
print(np.matmul(X, Y))
