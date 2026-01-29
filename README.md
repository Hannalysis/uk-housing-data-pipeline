# uk-housing-data-pipeline

# Project Supplements

- Primary dataset sourced from https://www.gov.uk/
- Secondary dataset sourced from https://www.ons.gov.uk/peoplepopulationandcommunity/housing/datasets/

# ETL

# Primary dataset (HM Land Registry Price Paid Data)

With Q1-Q4 downloaded as a CSV UTF-8:

combine_quarters.py > region_select_east_anglia.py > prepare_region_data.py

# Secondary dataset (ONS Ratio - House price : Residence Based Earnings)

With aff2ratioofhousepricetoresidencebasedearnings.xlsx converted to a google sheet and downloaded as 3 CSVs (5a, 5b, 5c):

combine_5a_to_5c.py > filter_year.py > region_and_subregion_select.py > prepare_region_and_subregion_data.py

...then load both cleaned files into a Tableau workbook