import random
import numpy as np
import matplotlib.pyplot as plt

length_theta = int(10e+4)
canvas_length = int(100)
balance_num = 10

theta = np.linspace(np.pi / 2, np.pi, length_theta)

canvas = np.zeros((canvas_length, canvas_length))
circle_canvas = np.copy(canvas)

radius = canvas_length - balance_num

x = np.ceil(np.cos(theta) * radius).astype('int')
y = np.ceil(np.sin(theta) * radius).astype('int')

for i, j in zip(x, y):
    circle_canvas[i, j] = 1

trial_num_at_epoc = int(500)
added_num = 1

def draw_circle(arr):
    for i, j in zip(x, y):
        arr[i, j] = np.max(arr)
    return arr

def one_epoc(arr):
    random_list = np.random.randint(0, canvas_length, trial_num_at_epoc * 2)
    index_list = np.array([[random_list[2 * i], random_list[(2 * i) + 1]] for i in range(trial_num_at_epoc)])
    for i in index_list:
        arr[i[0], i[1]]+=added_num
    return arr

circle_border = np.where(canvas == 1)

epoc_num = int(100)

sleep_time = 10e-3

for i in range(epoc_num):
    canvas = one_epoc(canvas)
    #canvas = draw_circle(canvas)　これやるとめちゃ重くなる
    plt.imshow(canvas, cmap='coolwarm')
    #plt.clim(0, np.max(canvas))
    plt.draw()
    plt.pause(sleep_time)
    plt.cla()

print(canvas)

plt.imshow(canvas, cmap='coolwarm')
#plt.clim(0, np.max(canvas))
plt.show()