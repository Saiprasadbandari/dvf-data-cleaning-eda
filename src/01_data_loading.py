import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")

files = sorted(RAW_DIR.glob("*.txt.zip"))

print("Files found:")
for file in files:
    print(file.name)

dfs = []

for file in files:
    print("Loading:", file.name)
    temp_df = pd.read_csv(file, sep="|", low_memory=False)
    temp_df["source_file"] = file.name
    dfs.append(temp_df)

df = pd.concat(dfs, ignore_index=True)

print("Final shape:", df.shape)
print(df.head())
print(df.info())