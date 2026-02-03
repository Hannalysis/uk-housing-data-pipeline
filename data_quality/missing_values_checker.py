import pandas as pd
import logging
from pathlib import Path

# --- Configure logging ---

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# -------------------------

# Place any csv path to be checked here
CSV_FILE = Path("data/fully_processed/primary/east_anglia_region.csv")

FILENAME = CSV_FILE.stem
OUTPUT_FILE = Path(f"data_quality/logs/missing_values_{FILENAME}.csv")

df = pd.read_csv(CSV_FILE)

# Check for any missing values

missing_counts = df.isnull().sum()
missing_counts = missing_counts[missing_counts > 0]

if not missing_counts.empty:

    logging.info("Columns with missing values:\n%s", missing_counts)
    
    # Saving to a CSV in the logs folder

    missing_counts_df = missing_counts.to_frame(name='missing_count')
    missing_counts_df['timestamp'] = pd.Timestamp.now().floor('s')
    missing_counts_df.to_csv(OUTPUT_FILE)
    logging.info("Missing values summary saved to '%s'", OUTPUT_FILE)
    
else:
    logging.info("No missing values found.")