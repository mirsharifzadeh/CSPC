import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

np.set_printoptions(suppress=True, precision=4)

t, x, y = np.loadtxt("trajectory.csv", float, None, ",", None, 1, None, True)

print(t)
print(x)
print(y)

v_x = np.gradient(x, t)
v_y = np.gradient(y, t)

a_x = np.gradient(v_x, t)
a_y = np.gradient(v_y, t)

v_x_recovered = cumulative_trapezoid(a_x, t, initial=0) + v_x[0]
v_y_recovered = cumulative_trapezoid(a_y, t, initial=0) + v_y[0]

fig, (x_y, v_t) = plt.subplots(nrows=2, ncols=1, figsize = (8, 8))
x_y.plot(x, y)
x_y.set_xlabel("X Position")
x_y.set_ylabel("Y Position")
x_y.set_title("X vs Y (Noisy)")

v_t.plot(t, np.sqrt(v_x_recovered**2 + v_y_recovered**2))
v_t.set_xlabel("Time")
v_t.set_ylabel("Speed")


plt.savefig("2dmotion.png")

plt.show()


