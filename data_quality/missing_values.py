import pandas as pd

# Place any csv path to be checked here
CSV_FILE = "data/processed/primary/combined_Qs.csv"

df = pd.read_csv(CSV_FILE)

# Check for missing values
missing_counts = df.isnull().sum()

# Filter only columns with missing values
missing_counts = missing_counts[missing_counts > 0]

if not missing_counts.empty:
    print("Columns with missing values:")
    print(missing_counts)
else:
    print("No missing values found.")