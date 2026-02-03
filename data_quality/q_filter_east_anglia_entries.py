import pandas as pd

# Place any path to the CSV file to be checked here
CSV_FILE = "data/processed/primary/combined_Qs.csv"
QUARTER = "Q4"

df = pd.read_csv(CSV_FILE)

# Filter quarterly data
df_quarter = df[df['Quarter'] == QUARTER]

# Postcode prefixes for East Anglia
east_anglia_postcodes = ["CB", "NR", "IP", "CO"]  # Cambridge, Norwich, Ipswich, Colchester

# Filter rows whose postcode starts with any of the East Anglia postcodes
df_q_postcode = df_quarter[df_quarter['Postcode'].str.replace(" ", "").str.upper().str[:2].isin(east_anglia_postcodes)]

print(f"Rows in East Anglia for {QUARTER}: {len(df_q_postcode)}")
print (df_q_postcode.head())
print("Filtered CSV shape:", df_q_postcode.shape)