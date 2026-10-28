import pandas as pd
from scipy import stats


df = pd.read_csv("chemicals_cancer.csv")

r_benz, p_benz = stats.pearsonr(df["benzene"], df["malignancy"])
r_cadm, p_cadm = stats.pearsonr(df["cadmium"], df["malignancy"])

print(f"Benzene vs Malignancy: r = {r_benz:.3f}, p = {p_benz:.4f}")
print(f"Cadmium vs Malignancy: r = {r_cadm:.3f}, p = {p_cadm:.4f}")

# Cause

high_polluts = (df["pollution_index"] > 40) & (df["pollution_index"] < 60)
r_hp_benz, _ = stats.pearsonr(df[high_polluts]["benzene"], df[high_polluts]["malignancy"])
print("Benzene (hp):", r_hp_benz)

r_hp_cadm, _ = stats.pearsonr(df[high_polluts]["cadmium"], df[high_polluts]["malignancy"])
print("Cadmium (hp):", r_hp_cadm);

