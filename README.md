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

---

## PW2 - Lab B: Optimization in Chemistry

**What I built:**
- I created three Python scripts (`warmup.py`, `kinetics.py`, `equilibrium.py`, and the bonus `titration.py`) to explore numerical optimization methods and apply them to chemistry problems such as rate constant fitting, chemical equilibrium calculation, and titration equivalence point detection.

**Comparison of Optimization Methods (Warmup & Harder Landscape):**
- In `warmup.py`, for the simple convex function $f(x) = (x-3)^2 + 1$, all three methods (Gradient Descent, Newton's method, and SLSQP) successfully converged to the global minimum at $x \approx 3$.
- In the harder landscape $g(x) = x^4 - 3x^2 + x + 5$, the results depended heavily on the initial point ($x_0$):
  - Starting from $x_0 = 0$, Newton's method converged to a local maximum/stationary point ($g''(x) < 0$), whereas SLSQP and Gradient Descent found local minima.
  - Starting from $x_0 = 2$, the methods converged toward the global minimum.
  - This demonstrates that while all methods agree on simple convex functions, algorithm choice and starting point are critical on non-convex landscapes.

**Chemistry Applications & Results:**
- **Reaction Rate Fitting (`kinetics.py`):** Minimizing the squared error between the first-order decay model $C(t) = C_0 e^{-kt}$ and the noisy measurements yielded a fitted rate constant $k \approx 0.25$. The generated plot (`kinetics.png`) confirms that the fitted curve accurately aligns with the data.
- **Chemical Equilibrium (`equilibrium.py`):** Solving the equilibrium condition for $H_2 + I_2 \rightleftharpoons 2HI$ via both root-finding (`scipy.optimize.newton`) and SLSQP minimization resulted in the same extent of reaction $x \approx 0.66$. The equilibrium amounts obtained were $n_{H_2} \approx 0.34\text{ mol}$, $n_{I_2} \approx 0.34\text{ mol}$, and $n_{HI} \approx 1.33\text{ mol}$ (`equilibrium.png`).
- **Titration Equivalence Point (`titration.py`):** Computed the derivative $d(\text{pH})/dV$ using `np.gradient`. The maximum slope (`np.argmax`) identified the equivalence point at approximately $50\text{ mL}$, corresponding to the sharpest pH jump (`titration.png`).

**Conclusion:**
- Optimization techniques allow us to effectively solve non-linear chemical problems, from parameter estimation to equilibrium composition. However, attention must be paid to initial conditions and second-derivative checks ($g''(x) > 0$) to ensure convergence to true physical minima rather than arbitrary stationary points.

---

---

## PW3 - Data, Distributions, Testing, and Causation

**What I built:**
- To evaluate whether the continuous variables in the dataset (`age`, `chol`, `trestbps`, and `thalach`) follow a normal distribution, both graphical checks (histograms and Q-Q plots) and theoretical expectations were analyzed.

#### Variable-by-Variable Verdicts:

1. **`age` (Age)**
   - **Verdict:** Approximately Normal
   - **Reasoning:** The histogram shows a fairly symmetric bell-shaped curve centered around 55 years. In the Q-Q plot, the data points closely align with the red theoretical reference line, with minimal deviations only at the extreme tails.

2. **`chol` (Serum Cholesterol)**
   - **Verdict:** Non-Normal (Right-Skewed)
   - **Reasoning:** The distribution exhibits a clear right skew (positive skewness). While the central bulk follows an approximate pattern, the Q-Q plot reveals significant upward deviation on the upper tail, caused by extreme outliers (values exceeding 400–500 mg/dl).

3. **`trestbps` (Resting Blood Pressure)**
   - **Verdict:** Moderately Right-Skewed / Non-Normal
   - **Reasoning:** The histogram demonstrates a rightward tail with distinct peaking/discretization around standard clinical measurements. The Q-Q plot shows noticeable upward curvature at higher values, indicating that higher blood pressure values depart from a strict normal distribution.

4. **`thalach` (Maximum Heart Rate Achieved)**
   - **Verdict:** Approximately Normal (Slightly Left-Skewed)
   - **Reasoning:** The data closely follows the diagonal reference line across the majority of quantiles in the Q-Q plot. The histogram displays a mostly symmetric spread centered around 150 bpm, despite a minor leftward tail at the lower extreme.

---

**Are Datas Normally Distributed?**
- While `age` and `thalach` can be treated as **approximately normal**, `chol` and `trestbps` deviate from normality due to right-skewness and outliers. This distinction will guide the choice between parametric and non-parametric statistical methods in Session 2.

### Is the Effect Real? (Comparing Heart Rate between Patient Groups)

To determine whether heart-disease patients reach a significantly different maximum heart rate (`thalach`) compared to healthy individuals, the dataset was split into two independent groups based on the `target` variable (`target = 1` for heart disease patients, `target = 0` for healthy patients).

#### Methodology
Based on the Session 1 findings where `thalach` was identified as approximately normally distributed, a two-sample **Welch's t-test** (`equal_var=False`) was conducted. Welch's t-test was chosen because it does not assume equal variances between the two groups, making it a robust parametric method for medical sample comparisons.

#### Numerical Results
- **Healthy Group Mean (`target = 0`):** 158.38 bpm
- **Disease Group Mean (`target = 1`):** 139.26 bpm
- **t-statistic:** 7.9636
- **p-value:** $3.4570 \times 10^{-14}$ (or $p < 0.001$)

#### Conclusion
The difference in maximum heart rate between heart-disease patients and healthy individuals is **statistically significant** ($p \approx 3.46 \times 10^{-14}$, which is far below the standard threshold of $\alpha = 0.05$). On average, patients with heart disease reach a noticeably lower maximum heart rate ($\approx 139.26$ bpm) compared to healthy individuals ($\approx 158.38$ bpm), confirming that the observed effect is real and not a result of random sample variation.

### Quantifying Uncertainty on Group Means

To assess the precision of the estimated group means for maximum heart rate (`thalach`), the **Standard Error of the Mean (SEM)** and **95% Confidence Intervals (CIs)** were calculated for both groups:

- **Healthy Group (`target = 0`):**
  - **Mean `thalach`:** $158.38$ bpm
  - **95% Confidence Interval:** $[155.12, 161.64]$ bpm (or $\pm \text{SEM}$)
- **Disease Group (`target = 1`):**
  - **Mean `thalach`:** $139.26$ bpm
  - **95% Confidence Interval:** $[135.75, 142.77]$ bpm (or $\pm \text{SEM}$)

#### Agreement with t-test Conclusion
Yes, the plot strongly agrees with the Welch's t-test conclusion reached above:
1. **Clear Separation:** The 95% confidence interval error bars of the two groups do not overlap at all. 
2. **Distinct Populations:** The non-overlapping error bars visually confirm that the average maximum heart rate for heart-disease patients is distinctly lower than that for healthy individuals, demonstrating that the observed difference is statistically robust and meaningful.

### Do two things move together?
There is not strong relation between age and thalach. "pearsonr" method was used for this test from stats library.
### Dataset 2 - A chemical-exposure mystery 

#### The Naive Analysis

* **Method:** Pearson correlation coefficients ($r$) and $p$-values were calculated between each chemical (`benzene`, `cadmium`) and `malignancy`.
* **Results:**
  * **Cadmium vs. Malignancy:** $r \approx 0.880$, $p < 0.0001$
  * **Benzene vs. Malignancy:** $r \approx 0.385$, $p < 0.0001$
* **Interpretation:** Taken at face value, **Cadmium** appears to be the primary cause of malignancy, as its correlation coefficient is substantially higher than that of Benzene.

#### Looking again for confounder effect

* **Method:** To control for potential confounders (`pollution_index` / `age`), the dataset was filtered to a subset with similar confounder values, effectively holding the third variable constant while recomputing associations.
* **Results:** Once the confounding variable was held constant, Cadmium's correlation dropped significantly ($r \approx 0.316$), but the correlation of Benzene increased ($r \approx 0.702$) whereas Benzene's true association emerged.
* **Interpretation:**
  * **Looks the main reason at first:** **Cadmium** — Its initial strong association was merely a spurious correlation driven by the background confounder.
  * **Real Cause:** **Benzene** — Demonstrates the true underlying causal link once the confounding effect is controlled.

## Conclusion:

### 1. Heart Disease Analysis (`heart.csv`)
* **Distribution & Normality:** Continuous variables (`age`, `chol`, `trestbps`, `thalach`) were evaluated via Q-Q plots and Shapiro-Wilk testing to determine the appropriate parametric vs. non-parametric testing pipeline.
* **Group Differences (`thalach` vs. `target`):** Hypothesis testing alongside Standard Error (SE) confidence intervals confirmed a statistically significant difference in maximum heart rate between patients with heart disease and healthy individuals.
* **Age vs. Heart Rate:** A clear negative correlation was observed, indicating that maximum heart rate (`thalach`) systematically declines with increasing `age`.

### 2. Chemical Exposure Mystery (`chemicals_cancer.csv`)
* **Naive Analysis:** Initial unadjusted Pearson correlation suggested **Cadmium** was the primary cause of malignancy ($r \approx 0.880$) compared to **Benzene** ($r \approx 0.385$).
* **Confounder Control:** After filtering and holding the confounding variable (`pollution_index`) constant, Cadmium's association dropped significantly, revealing its initial strength to be a **spurious correlation** driven by environmental pollution.
* **Causal Verdict:** **Benzene** is the true causal driver of malignancy. Controlling for the confounder closed the backdoor path and isolated the genuine direct effect.

---