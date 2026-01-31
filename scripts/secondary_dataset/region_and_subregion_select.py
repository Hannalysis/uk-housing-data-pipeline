import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
processed_secondary_folder = PROJECT_ROOT / "data/processed/secondary"
fully_processed_secondary_folder = PROJECT_ROOT / "data/fully_processed/secondary"

combined_ONS = pd.read_csv(processed_secondary_folder / 'combined_ONS_filtered_years.csv')

# Initial filter for only East of England Region
east_of_england_df = combined_ONS[combined_ONS['Country/Region name'] == 'East of England']

# State the areas outside of East Anglia and place them into a list to exclude

exclude_las = [
    'Dacorum', 'Watford', 'Three Rivers', 'St Albans', 'East Hertfordshire', 
    'North Hertfordshire', 'Stevenage', 'Welwyn Hatfield', 'Hertsmere',  # Hertfordshire
    'Bedford', 'Central Bedfordshire', 'Luton',  # Bedfordshire
    'Basildon', 'Castle Point', 'Southend-on-Sea', 'Thurrock', 
    'Harlow', 'Brentwood', 'Rochford', 'Maldon', 'Epping Forest', 'Chelmsford'  # Southern Essex
]

# New df for East Anglia only
east_anglia_ons_df = east_of_england_df[~east_of_england_df['Local authority name'].isin(exclude_las)]

# Saving
east_anglia_ons_df.to_csv(fully_processed_secondary_folder / 'combined_ONS_filtered_years_filtered_regions.csv', index=False)

print(east_anglia_ons_df.shape)
print(east_anglia_ons_df.head())