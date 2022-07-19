import numpy as np
import matplotlib.pyplot as plt

canvas_size = (1, 1000, 1000)
canvas = np.zeros(canvas_size)

radius = 200

theta = np.linspace(0, 2 * np.pi, int(10e+3))

#convert float to int
convert_float_to_int_for_ndarray = np.frompyfunc(int, 1, 1)
x = (np.cos(theta) * radius).astype(np.int64)
y = (np.sin(theta) * radius).astype(np.int64)

plt.plot(x, y)
plt.show()


#replace_canvas = np.frompyfunc()