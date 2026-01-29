# uk-housing-data-pipeline

# ETL

# Primary dataset (HM Land Registry Price Paid Data)

Dataset downloaded in CSV UTF-8 so we move on straight to:

combine_quarters.py > region_select_east_anglia.py > prepare_region_data.py

# Secondary dataset (ONS Ratio - House price : Residence Based Earnings)

Convert xslx file to csv utf-8 (convert_xlsx_to_csv_utf8.py), and then:

filter_year.py > region_and_subregion_select.py > prepare_region_and_subregion_data.py

...then load both cleaned files into a Tableau workbook