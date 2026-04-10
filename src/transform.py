import pandas as pd
import logging


def validate_data(df):
    issues = {}

    issues['duplicates'] = df.duplicated().sum()

    issues['invalid_dates'] = pd.to_datetime(
        df['date_joined'], errors='coerce'
    ).isnull().sum()

    issues['missing_values'] = df.isnull().sum().to_dict()
    issues['negative_balances'] = (df['account_balance'] < 0).sum()
    return issues


def clean_data(df):
    logging.info("Cleaning data")

    df = df.drop_duplicates()
    df = df.dropna()
    df['date_joined'] = pd.to_datetime(df['date_joined'], errors='coerce')
    df = df.dropna(subset=['date_joined'])
    df = df[df['account_balance'] >= 0]
    return df

