"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

def k_imbalance(x):
    return ((2*x)**2)/((a-x)*(b-x)) - K

def k_imbalance2(x):
    return (((2*x)**2)/((a-x)*(b-x)) - K)**2

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

x_newton = newton(k_imbalance, x0 = 0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.

x_minimize = minimize(k_imbalance2, x0 = [0.5], bounds=[(0, 0.999)], method="SLSQP")

print("Newton Method Result:", x_newton)
print("SLSQP Method Result:", format(x_minimize.x[0], '.15f'))


# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

x_eq = x_newton

n_H2_eq = 1 - x_eq
n_I2_eq = 1 - x_eq
n_HI_eq = 2 * x_eq

print(f"Equilibrium amounts:")
print(f"H2: {n_H2_eq:.4f} mol")
print(f"I2: {n_I2_eq:.4f} mol")
print(f"HI: {n_HI_eq:.4f} mol")

x_vals = np.linspace(0, 0.99, 200)
nH2 = a - x_vals
nI2 = b - x_vals
nHI = 2 * x_vals

plt.figure(figsize=(8, 5))

plt.plot(x_vals, nH2, label = "H2 (1 - x)", color = 'blue')
plt.plot(x_vals, nI2, label = "I2 (1 - x)", color = 'red', linestyle = '--')
plt.plot(x_vals, nHI, label = "HI (2x)", color = "green")

plt.axvline(x=x_eq, color='black', linestyle=':', label=f'Equilibrium (x = {x_eq:.3f})')

plt.xlabel('Extent of reaction (x)')
plt.ylabel('Amount (moles)')
plt.title('Chemical Equilibrium: H2 + I2 <=> 2 HI')
plt.grid(True)
plt.legend()

plt.savefig('equilibrium.png')
plt.show()