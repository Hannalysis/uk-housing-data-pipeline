import csv
from collections import Counter

# Place any path to the CSV file to be checked here
CSV_FILE = "data/processed/primary/combined_Qs.csv"

with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    counts = [len(row) for row in reader]

counter = Counter(counts)

for cols, rows in sorted(counter.items()):
    print(f"{rows} row(s) have {cols} columns")