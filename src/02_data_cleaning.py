import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Find DVF files
files = sorted(RAW_DIR.glob("*.txt.zip"))

print("Raw directory:", RAW_DIR)
print("Files found:", len(files))

if len(files) == 0:
    raise FileNotFoundError(
        "No .txt.zip files found in data/raw folder"
    )

# Load files
dfs = []

for file in files:
    print("Loading:", file.name)

    temp_df = pd.read_csv(
        file,
        sep="|",
        low_memory=False
    )

    temp_df["source_file"] = file.name

    dfs.append(temp_df)

# Merge all years
df = pd.concat(dfs, ignore_index=True)

print("\nOriginal shape:", df.shape)

# Missing value report
missing_report = pd.DataFrame({
    "missing_count": df.isnull().sum(),
    "missing_percentage": (
        df.isnull().sum() / len(df)
    ) * 100
})

missing_report = missing_report.sort_values(
    by="missing_percentage",
    ascending=False
)

print("\nTop 20 columns with missing values:")
print(missing_report.head(20))

# Drop columns with >80% missing values
columns_to_drop = missing_report[
    missing_report["missing_percentage"] > 80
].index

print("\nColumns dropped:")
print(list(columns_to_drop))

df_clean = df.drop(columns=columns_to_drop)

print("\nCleaned shape:", df_clean.shape)

# Convert date column
df_clean["Date mutation"] = pd.to_datetime(
    df_clean["Date mutation"],
    format="%d/%m/%Y",
    errors="coerce"
)

# Convert property value from French format to numeric
df_clean["Valeur fonciere"] = (
    df_clean["Valeur fonciere"]
    .astype(str)
    .str.replace(",", ".", regex=False)
)

df_clean["Valeur fonciere"] = pd.to_numeric(
    df_clean["Valeur fonciere"],
    errors="coerce"
)

# Remove rows with missing important values
df_clean = df_clean.dropna(
    subset=["Date mutation", "Valeur fonciere"]
)

# Remove duplicate rows
df_clean = df_clean.drop_duplicates()

print("\nShape after date/price conversion and duplicate removal:")
print(df_clean.shape)

# Save a small clean sample for EDA
sample_path = PROCESSED_DIR / "dvf_clean_sample.csv"
df_clean.head(100000).to_csv(sample_path, index=False)

print("\nSaved cleaned sample to:")
print(sample_path)