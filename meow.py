from operator import length_hint
import numpy as np
import matplotlib.pyplot as plt

length_theta = int(10e+4)
canvas_length = int(10e+2)
balance_num = 10

theta = np.linspace(np.pi / 2, np.pi, length_theta)

canvas = np.zeros((canvas_length, canvas_length))

radius = canvas_length - balance_num

x = np.ceil(np.cos(theta) * radius).astype('int')
y = np.ceil(np.sin(theta) * radius).astype('int')

for i, j in zip(x, y):
    canvas[i, j] = 100

print(canvas)

plt.imshow(canvas, cmap='cool')
plt.show()