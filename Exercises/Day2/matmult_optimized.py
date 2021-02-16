import numpy as np

@profile
def X(N): return np.random.randint(100, size=(N, N))

@profile
def Y(N): return np.random.randint(100, size=(N, N + 1))

@profile
def multiply(X, Y): return np.matmul(X, Y)

@profile
def print_results(result): print(result)

N = 250
print_results(multiply(X(N), Y(N)))
