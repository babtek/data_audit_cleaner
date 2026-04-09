import pandas as pd
import logging
import os

# Create log folder if needed
os.makedirs("log", exist_ok=True)


logging.basicConfig(
    filename="log/data_audit_cleaner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_data(df):
    issues = {}

    # Invalid dates
    invalid_dates = df['date_joined'].apply(
        lambda x: pd.to_datetime(x, errors='coerce')
    ).isnull().sum()
    issues['invalid_dates'] = invalid_dates

    # Missing values
    issues['missing_values'] = df.isnull().sum().to_dict()

    # Negative balances
    negative_balances = (df['account_balance'] < 0).sum()
    issues['negative_balances'] = negative_balances

    # Invalid validated field (not True/False)
    invalid_validated = ~df['validated'].isin([True, False])
    issues['invalid_validated'] = invalid_validated.sum()
    return issues


def audit_data(df):
    report = {}
    report["rows"] = len(df)
    report["duplicates"] = df.duplicated().sum()
    report["missing_values"] = df.isnull().sum().to_dict()
    return report


def clean_data(df):
    logging.info("Cleaning data")

    df = df.drop_duplicates()
    df = df.dropna()

    # Fix date format
    df['date_joined'] = pd.to_datetime(df['date_joined'], errors='coerce')

    # Remove invalid dates
    df = df.dropna(subset=['date_joined'])

    # Remove negative balances
    df = df[df['account_balance'] >= 0]

    return df


def main():
    logging.info("Loading data")

    df = pd.read_csv("data/sample.csv")

    logging.info(f"Loaded {len(df)} rows")

    validation_report = validate_data(df)
    logging.info(f"Validation report: {validation_report}")

    clean_df = clean_data(df)

    os.makedirs("reports", exist_ok=True)

    clean_df.to_csv("reports/cleaned.csv", index=False)

    with open("reports/report.txt", "w") as f:
        f.write(str(validation_report))

    logging.info("Processing complete")


if __name__ == "__main__":
    main()