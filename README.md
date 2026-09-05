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
