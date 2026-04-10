## ETL Pipeline Overview

This project implements a simple ETL pipeline:

- **Extract**: Reads raw CSV data
- **Transform**: Validates and cleans data (duplicates, missing values, invalid dates)
- **Load**: Outputs cleaned dataset and validation report

## Features
- Modular pipeline design
- Config-driven execution
- Logging for traceability
- Data validation and cleaning

## Run
python src/main.py