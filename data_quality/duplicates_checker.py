import pandas as pd

# Place any path to the CSV file to be checked here
CSV_FILE = "data/processed/primary/combined_Qs.csv"

# Load CSV into a DataFrame
df = pd.read_csv(CSV_FILE)

# Check for duplicate rows
duplicates = df.duplicated(keep=False)  # mark all duplicates
num_duplicates = duplicates.sum()

print(f"Total rows: {len(df)}")
print(f"Duplicate rows: {num_duplicates}")
print(f"Unique rows: {len(df) - num_duplicates}")

if num_duplicates > 0:
    print("\nAll duplicate rows:")
    print(df[duplicates])
else:
    print("No duplicate rows found")