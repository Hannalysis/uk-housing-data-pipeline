<h1 align = "center">UK Housing Data Pipeline</h1>

<p align = "center"><b>Overview</b>: This project contains a mostly modular, incremental Python data pipeline for UK housing analysis, combining HM Land Registry Price Paid Data with ONS affordability ratios (Tables 5b and 5c).

The pipeline is designed so that any script can be run independently or as part of the full workflow. At any stage, outputs are analytics-ready and structured for direct ingestion into Tableau. </p>

<p align = "center">
  <img src= "/readme-images/house-icon.jpg"             alt="house-icon-outline"
  width="25%"/>
</p>

**ℹ Note:** The full pipeline currently focuses on extracting the relevant housing dataset for the East Anglian region, a subregion of the East of England.

------------

<h2>Table of Contents</h2>


- [Installation](#installation)
- [Supplements](#documentation)
- [Tech Stack](#tech-stack)
- [ETL Pipeline](#etl-pipeline)
- [Data Quality](#data-quality)
- [Author](#author)

------------

# Installation

Create the virtual environment
```bash
python -m venv .venv
```
and run it
```bash
source .venv/bin/activate
``` 
OR
```shell (windows)
.venv\Scripts\activate
```
and install dependencies (Pandas only)
```bash
pip install -r requirements.txt
```

# Project Supplements

- Primary dataset sourced from https://www.gov.uk/government/organisations/land-registry
(Note: The data obtained may have been adjusted or sandboxed for testing purposes)

- Secondary dataset sourced from https://www.ons.gov.uk/peoplepopulationandcommunity/housing/datasets/

# Tech Stack

<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,vscode&perline=8" />
  </a>
  <h4><u>Main modules:</u><br/><span style = "font-weight:lighter">pandas</span></h4>
  <h4><u>Script modules:</u><br/><span style = "font-weight:lighter">pathlib, collections, csv</span></h4>
</p>

# ETL

# Primary dataset (HM Land Registry Price Paid Data)

With <i>Q1-Q4</i> downloaded as a <i>CSV UTF-8</i>:

combine_quarters_2023.py* > region_select_east_anglia.py

Note: *2023 required a bespoke combine script as there were misaligned columns in Q4 and different date format in Q2.

Assuming all quarters from other years are utilising the exact same layout of columns, combine_quarters.py would be apt:

| Step | Script            | Input                  | Output                         |
|-----:|----------------------|------------------------|--------------------------------|
| 1    | combine_quarters.py     |     data/raw/primary/YYYY-Q1.csv (to YYYY-Q4)         | data/processed/primary/combined_Qs.csv            |
| 2    | region_select_east_anglia.py      | combined_Qs.csv     | data/fully_processed/primary/east_anglia_region.csv |


# Secondary dataset (ONS Ratio - House price : Residence Based Earnings)

With <i>aff2ratioofhousepricetoresidencebasedearnings.xlsx</i> converted to a google sheet and downloaded as 2 CSVs (5b & 5c):

combine_5b_to_5c.py > filter_year.py > region_and_subregion_select.py

...then load both cleaned files into a Tableau workbook

| Step | Script            | Input                  | Output                         |
|-----:|----------------------|------------------------|--------------------------------|
| 1    | combine_ons_5b_to_5c.py     |  data/raw/secondary/5b.csv (and 5c)*            |   data/processed/secondary/combined_ONS.csv          |
| 2    | filter_year.py      | combined_ONS.csv      | data/processed/secondary/combined_ONS_filtered_years.csv |
| 3    | region_and_subregion_select.py      | combined_ONS_filtered_years.csv     | data/fully_processed/combined_ONS_filtered_years_filtered_regions.csv |

Note: *Where: <br>
5b.csv = <i>Median_gross_annual_residence_based_earnings_by_local_authority_district_5b.csv</i> <br>
5c.csv = <i>Ratio_of_median_house_price_to_median_gross_annual_residence_based_earnings_by_local_authority_district_5c.csv</i>

# Data Quality



# Author
Created by Hannahry
<i></br><b>aka: </b>@Hannalysis</i>