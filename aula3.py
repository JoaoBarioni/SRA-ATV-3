import numpy as np
import math

x1 = 5
x2 = 3
l = 0.5
z = math.pi
V1 = 2
r = 0.25
W1 = 3
L = 1
Xangulo = np.array([2, 1, math.pi])
t = 1
X0 = 0

A = np.array([[(r * x1) / 2 + (r * x2) / 2],
              [0],
              [(r * x1) / (2 * l) - (r * x2) / (2 * l)]])

B = np.array([[math.cos(z), -math.sin(z), 0],
              [math.sin(z), math.cos(z), 0],
              [0, 0, 1]])

Y = np.dot(B, A)

print(Y)
