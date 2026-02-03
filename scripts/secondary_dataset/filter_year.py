import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
processed_secondary_folder = PROJECT_ROOT / "data/processed/secondary"

combined_ONS = pd.read_csv(processed_secondary_folder / 'combined_ONS.csv')

# Year selection range
START_YEAR = 2013
END_YEAR = 2024

# Filter for the specified year range

combined_ONS['year'] = combined_ONS['year'].astype(int)
combined_ONS = combined_ONS[(combined_ONS['year'] >= START_YEAR) & (combined_ONS['year'] <= END_YEAR)]

# Saving the filtered dataset
combined_ONS.to_csv(processed_secondary_folder / 'combined_ONS_filtered_years.csv', index=False)

print("Filtered ONS CSV shape:", combined_ONS.shape)
print(combined_ONS.head())