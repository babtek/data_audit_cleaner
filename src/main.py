import logging
import json
import os

from extract import extract_data
from transform import validate_data, clean_data
from load import load_data, save_report

# Logging setup
os.makedirs("log", exist_ok=True)

logging.basicConfig(
    filename="log/data_audit_cleaner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_config():
    with open("config.json") as f:
        return json.load(f)


def run_pipeline():
    config = load_config()

    logging.info("Starting ETL pipeline")

    df = extract_data(config["input_file"])

    validation_report = validate_data(df)
    logging.info(f"Validation report: {validation_report}")

    clean_df = clean_data(df)

    load_data(clean_df, config["output_file"])
    save_report(validation_report, config["report_file"])

    logging.info("ETL pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()