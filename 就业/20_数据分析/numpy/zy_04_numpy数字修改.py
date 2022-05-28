import numpy as np

t = np.array(range(24))

t = t.reshape((4,6))

print(t)

print(np.where(t <= 3,100,200))

print(t.clip(10,18))