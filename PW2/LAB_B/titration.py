"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.

volume_base, pH = np.loadtxt("titration.csv", float, None, ",", None, 1, None, True)

print(volume_base)
print(pH)

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.

pH_slope = np.gradient(pH, volume_base)
V_max_slope = np.argmax(pH_slope)
print("Equivalence point", V_max_slope)



# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
    
fig, (pH_V, slope_V) = plt.subplots(nrows=1, ncols=2, figsize=(8, 8))

pH_V.plot(pH, volume_base, color="blue")
pH_V.set_xlabel("pH")
pH_V.set_ylabel("Volume")
pH_V.set_title("pH vs Volume")
pH_V.axhline(y=V_max_slope, color="black", linestyle=":")

slope_V.plot(pH_slope, volume_base, color="blue")
slope_V.set_xlabel("Slope")
slope_V.set_ylabel("Volume")
slope_V.set_title("Slope vs Volume")

plt.savefig("titration.png")