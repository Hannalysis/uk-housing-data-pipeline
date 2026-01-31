import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
secondary_data_folder = PROJECT_ROOT / "data/raw/secondary"


df_5b = pd.read_csv(secondary_data_folder / 'Median_gross_annual_residence_based_earnings_by_local_authority_district_5b.csv', skiprows=1)
df_5c = pd.read_csv(secondary_data_folder / 'Ratio_of_median_house_price_to_median_gross_annual_residence_based_earnings_by_local_authority_district_5c.csv', skiprows=1)

print("5b columns:", df_5b.columns.tolist())
print("5c columns:", df_5c.columns.tolist())

keep_columns = ['Country/Region code', 'Country/Region name', 'Local authority code', 'Local authority name']

# Identify year columns dynamically

year_cols_5b = [c for c in df_5b.columns if c not in keep_columns]
year_cols_5c = [c for c in df_5c.columns if c not in keep_columns]

# Melt 5b into long format

df_5b_long = df_5b.melt(
    id_vars=keep_columns,
    value_vars=year_cols_5b,
    var_name='year',
    value_name='median_gross_annual_earnings'
)

# Melt 5c into long format

df_5c_long = df_5c.melt(
    id_vars=keep_columns,
    value_vars=year_cols_5c,
    var_name='year',
    value_name='price_to_earnings_ratio'
)

# Merge long tables

df_combined_ons = pd.merge(
    df_5b_long,
    df_5c_long,
    on=keep_columns + ['year'],
    how='inner'
)

# Saving
df_combined_ons.to_csv(PROJECT_ROOT / "data/processed/secondary/combined_ONS.csv", index=False)

print("Combined long-format ONS 5b + 5c CSV ready!")
