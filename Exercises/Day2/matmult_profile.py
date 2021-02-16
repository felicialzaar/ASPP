# Program to multiply two matrices using nested loops
import random

# NxN matrix
@profile
def create_x(N):
  X = []
  for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])
  return X

# Nx(N+1) matrix
@profile
def create_y(N):
  Y = []
  for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])
  return Y

# iterate through rows of X
@profile
def multiply(N, X, Y):
  # result is Nx(N+1)
  result = []
  for i in range(N):
    result.append([0] * (N+1))
  for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
      # iterate through rows of Y
      for k in range(len(Y)):
        result[i][j] += X[i][k] * Y[k][j]
  return result

@profile
def print_results(result):
  for r in result:
    print(r)

N = 250
x = create_x(N)
y = create_y(N)
result = multiply(N, x, y)
print_results(result)
