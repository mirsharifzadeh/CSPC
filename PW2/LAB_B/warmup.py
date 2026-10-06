"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize
import matplotlib.pyplot as plt
# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")

# (1)
x0 = 0
decay = 0.95
lr = 0.5
tol = 0.001

while True:

  step = lr * df(x0)
  x0 = x0 - step
  lr = lr * decay
  print(x0)

  if(abs(step) < tol):
      break

print("Gradient Descent:", x0)

# (2)

Nmethod = newton(func=df, x0=0, fprime=d2f)
print("\nNewton Method with SciPy:", Nmethod)

# (3)

minimized = minimize(f, 0, method="SLSQP")
print("\nSLSQP Method", minimized.x[0])
print("\n")



# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?

# (1)

x0 = 0
decay = 0.95
lr = 0.1
tol = 0.001

while True:

    step = lr * dg(x0)
    x0 = x0 - step
    lr = lr * decay
    print(x0)

    if(abs(step) < tol):
        break

print("Gradient Descent:", x0)

# (2)

Nmethod = newton(func=dg, x0=0, fprime=d2g)
if d2g(Nmethod) > 0:
    print("\nLocal Minimum")
else:
    print("\nLocal Maximum")
print("Newton Method with SciPy:", Nmethod)

# (3)

minimized = minimize(g, 0, method="SLSQP")
print("\nSLSQP Method", minimized.x[0])
print("\n")

# x0 = 2

# (1)

x0 = 2
decay = 0.95
lr = 0.1
tol = 0.001

while True:

    step = lr * dg(x0)
    x0 = x0 - step
    lr = lr * decay
    print(x0)

    if(abs(step) < tol):
        break

print("Gradient Descent:", x0)

# (2)

Nmethod = newton(func=dg, x0=2, fprime=d2g)
if d2g(Nmethod) > 0:
    print("\nLocal Minimum")
else:
    print("\nLocal Maximum")
print("Newton Method with SciPy:", Nmethod)

# (3)

minimized = minimize(g, 2, method="SLSQP")
print("\nSLSQP Method", minimized.x[0])
print("\n")