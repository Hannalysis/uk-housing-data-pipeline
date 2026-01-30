import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
primary_data_folder = PROJECT_ROOT / "data/raw/primary"

# Using a constant so any year could be managed
YEAR = 2023

# Column names taken from the HM Land Registry documentation

COLUMNS_STANDARD = ['Transaction_ID', 'Price', 'Date of Transfer', 'Postcode', 'Property Type',
           'Old/New', 'Duration', 'PAON', 'SAON', 'Street', 'Locality', 'Town/City', 'District',
           'County', 'PPD Category Type', 'Record Status']

COLUMNS_Q4 = ['Transaction_ID', 'Price', 'Postcode', 'Property Type',
           'Old/New', 'Duration', 'PAON', 'SAON', 'Street', 'Locality', 'Town/City', 'District',
           'County', 'PPD Category Type', 'Record Status', 'Date of Transfer'] # Note: Date of Transfer is last in Q4 only

# List to store the collected but unsorted dataframes
dfs = []

# Looping through each quarterly CSV

for i in range(1, 5):
    file = primary_data_folder / f"{YEAR}_Q{i}.csv"
    df = pd.read_csv(file, header=None)

    if i == 4:
        cols = list(df.columns)

        # remove last column (Date of Transfer)
        date_of_transfer_col = cols.pop(-1)

        # insert it at the 3rd column
        cols.insert(2, date_of_transfer_col)
        df = df[cols]

    df.columns = COLUMNS_STANDARD

    # Adding a new column to track which quarter the row came from
    df["Quarter"] = f"Q{i}"
    dfs.append(df)

# Combine all quarters into a single dataframe
combined_df = pd.concat(dfs, ignore_index=True)

# Saving to the appropriate processed folder
combined_df.to_csv(PROJECT_ROOT / "data/processed/primary/combined_Qs.csv", index=False)

print("Combined CSV shape:", combined_df.shape)
print(combined_df.head())