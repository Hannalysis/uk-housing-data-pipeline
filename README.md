# uk-housing-data-pipeline

# Project Supplements

- Primary dataset sourced from https://www.gov.uk/
- Secondary dataset sourced from https://www.ons.gov.uk/peoplepopulationandcommunity/housing/datasets/

# ETL

# Primary dataset (HM Land Registry Price Paid Data)

With Q1-Q4 downloaded as a CSV UTF-8:

combine_quarters_2023.py* > region_select_east_anglia.py

Note: *2023 required a bespoke combine script as there were misaligned columns in Q4 and different date format in Q2.

Assuming all quarters from other years are utilising the exact same layout of columns, combine_quarters.py would be apt.

# Secondary dataset (ONS Ratio - House price : Residence Based Earnings)

With aff2ratioofhousepricetoresidencebasedearnings.xlsx converted to a google sheet and downloaded as 2 CSVs (5b & 5c):

combine_5b_to_5c.py > filter_year.py > region_and_subregion_select.py

...then load both cleaned files into a Tableau workbook