import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# loading dataset

df = pd.read_csv("heart.csv")

# shape and first row

shape = df.shape
head = df.head(1)

print("Shape:", shape)
print("First Row:", head)

# isolating

age = df["age"]
chol = df["chol"]
trestbps = df["trestbps"]
thalach = df["thalach"]

datas = [age, chol, trestbps, thalach]

# drawing histogram

'''

fig, (ageplt, cholplt, trestbpsplt, thalachplt) = plt.subplots(ncols=1, nrows=4, figsize=(10, 8))

ageplt.hist(age, bins = 35)
ageplt.set_xlabel("value")
ageplt.set_ylabel("how often")

cholplt.hist(chol, bins = 35)
cholplt.set_xlabel("value")
cholplt.set_ylabel("how often")

trestbpsplt.hist(trestbps, bins=35)
trestbpsplt.set_xlabel("value")
trestbpsplt.set_ylabel("how often")

thalachplt.hist(thalach, bins=35)
thalachplt.set_xlabel("value")
thalachplt.set_ylabel("how often")

plt.show()

'''
'''
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for col, ax in zip(datas, axes.flatten()):
    stats.probplot(col, dist="norm", plot=ax)

plt.tight_layout()
plt.show()
'''

# SESSION 2

healthy = df[df["target"] == 0]["thalach"]
disease = df[df["target"] == 1]["thalach"]

'''

t_stat, p = stats.ttest_ind(healthy, disease)

print(f"Disease mean thalach: {disease.mean():.2f}")
print(f"Healthy mean thalach: {healthy.mean():.2f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p:.4e}")

if p < 0.05:
    print("The difference between two groups is statistically significant")

else:
    print("The difference between two groups is not statistically significant")

'''

means = [healthy.mean(), disease.mean()]

sem_healthy = stats.sem(healthy)
sem_disease = stats.sem(disease)

ci_healthy = stats.t.interval(
    0.95, len(healthy) - 1, loc=healthy.mean(), scale=sem_healthy
)
ci_disease = stats.t.interval(
    0.95, len(disease) - 1, loc=disease.mean(), scale=sem_disease
)

ci_err_healthy = means[0] - ci_healthy[0]
ci_err_disease = means[1] - ci_disease[0]

print(f"Healthy Mean: {means[0]:.2f} ± {sem_healthy:.2f} (SEM)")
print(f"Disease Mean: {means[1]:.2f} ± {sem_disease:.2f} (SEM)")

groups = ["Healthy (target=0)", "Disease (target=1)"]
x_pos = np.arange(len(groups))

plt.figure(figsize=(7, 5))

plt.bar(x_pos, means, yerr=[ci_err_disease, ci_err_healthy], capsize=7, color=['blue', 'red'], alpha=0.8)

plt.xticks(x_pos, groups)
plt.ylabel("Mean Maximum Heart Rate (thalach)")
plt.title("Mean thalach by Group with 95% Confidence Intervals")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

r, p = stats.pearsonr(age, thalach)

if r == 0:
    print("No Relation")
elif r > 0.7:
    print("The things move together")
elif r < -0.7:
    print("The things move in opposite way")
else:
    print("Not Strong Relation")








