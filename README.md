# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW1/LAB_A/.

## Setup

Create the environment for a given lab:
conda env create -f PW1/LAB_A/environment.yml
conda activate cspc

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- I built tests for decay and speed.py file for comparison of pure python and numPy version.

**Speed comparison (loop vs NumPy):** (after 1000 tests)
- loop : 0.17312254107902117 s
- numpy : 0.00011340972495963797 s
- speed-up: 1526.52 x faster

**Tests:** all passing? YES

**Conclusion:**
- Tests passed correctly, simulation gives close values to scientific formula. I have observed that
- using numpy makes the simulation 1526.52 times faster rather using pure python code with loop.