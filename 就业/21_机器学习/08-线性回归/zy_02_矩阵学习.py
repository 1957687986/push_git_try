import numpy as np

a = [[1,2,3,4],
     [5,6,7,8],
     [2,3,7,9]]
b = [2,2,2,2]

c = np.multiply(a,b)

print(c)

b = [[2],[2],[2],[2]]

c = np.dot(a,b)

print(c)