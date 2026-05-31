import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "dvf_clean_sample.csv"

df = pd.read_csv(DATA_PATH)

print("Original shape:", df.shape)

Q1 = df["Valeur fonciere"].quantile(0.25)
Q3 = df["Valeur fonciere"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_no_outliers = df[
    (df["Valeur fonciere"] >= lower_bound)
    &
    (df["Valeur fonciere"] <= upper_bound)
]

print("Shape after outlier removal:", df_no_outliers.shape)
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)