import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
primary_data_folder = PROJECT_ROOT / "data/processed/primary"

# Load HM Land Registry data
df = pd.read_csv(primary_data_folder / "combined_Qs.csv")

# Postcode prefixes for East Anglia
east_anglia_postcodes = ["CB", "NR", "IP", "CO"]  # Cambridge, Norwich, Ipswich, Colchester

# Filter rows whose postcode starts with any of the East Anglia postcodes
df_postcode = df[df['Postcode'].str.replace(" ", "").str.upper().str[:2].isin(east_anglia_postcodes)]

# Save the region filtered data
df_postcode.to_csv(primary_data_folder / "east_anglia_region.csv", index=False)

print(f"Rows in East Anglia: {len(df_postcode)}")
print(df_postcode.head())