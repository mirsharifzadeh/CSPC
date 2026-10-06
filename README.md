# CSPC — Computer Science for Physics and Chemistry

My coursework repository for the course.
Each practical lives under `PW<n>/Lab <X>/`.

## Setup

Create and activate the environment for a given lab:

```bash
conda env create -f "PW<n>/Lab <X>/environment.yml"
conda activate cspc
```

Run the tests for a lab from inside its folder:

```bash
cd "PW<n>/Lab <X>"
pytest -v
```

---

## PW1 — Lab A: Reproducible Foundations

**What I built:**
- I built tests for decay and speed.py file for comparison of pure python and numPy version.

**Speed comparison (loop vs NumPy):**

| version | time (s) |
|---------|----------|
| pure-Python loop | 0.17312254107902117 |
| NumPy (vectorised) | 0.00011340972495963797 |

- Speed-up: **1526.52  × faster**

**Tests:** all passing? YES

**Conclusion:**
- Tests passed correctly, simulation gives close values to scientific formula.
- I have observed that
using numpy makes the simulation 1526.52 times faster rather using pure python code with loop.

---

---

## PW1 — Lab B: Data, Plotting, and Automation

**What I built:**
- I built a python program that reads values from csv file and draw the plot according to values. And then automated this process with Snakemake.

**Conclusion:**
- We are using mathplotlib library in order to draw plots.
- We are using loadtxt from NumPy library to write the values from .csv file.

---

---

## PW2 — Lab A: Motion from Tracking Data

**What I built:**
- I built analysis.py which takes free fall time and position values and gives velocity and acceleration. At the end it draws a graph with noisy and less noisier values.

**Derivation Noise Problem**
- Firstly freefall.csv was read into two arrays t and y. Then using np.gradient derivation was applied on y w.r.t t in order to get velocity. After applying the same procedure on v, acceleration was obtained. Last result (mean acceleration) was -8.5796875, which is not close to -9.81 enough. And also when its standard deviation is printed, 28.71 was obtained. It shows that double derivation makes our results noisy. Because derivation makes our results noisy, as the computer substract two nearly-equal y values and divide it by a small t.

**Noise comparison (Derivate and Integral):**
- In the second step obtained a was integrated in order to back velocity. Then after the same procedure for velocity gave us position. As we can observe on graph, the noise is less, graph of velocity and position are smoother than the previous one.

**Conclusion:**
- As we know from Calculus, derivation increases the noise, because when we find the m = 0 (m is slope) point, we should divide it very small number, so it gives us some errors and when we double this process, the error becomes more visible. This problem is also observed in computer, so we should solve it.

- This problem can be solved with integration. Because we know that integration is opposite of derivative and it is noise amplifier. After the integration applied to acceleration values and v, y recovered, this observed that the graphs became smoother and less noisier.

---
