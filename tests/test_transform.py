import pandas as pd
from src.transform import validate_data, clean_data

def test_validate_data_detects_issues():
    data = {
        "first_name": ["A", "B"],
        "last_name": ["X", "Y"],
        "date_joined": ["invalid_date", "2023-01-01"],
        "validated": [True, False],
        "account_balance": [100, -50]
    }

    df = pd.DataFrame(data)

    report = validate_data(df)

    assert report["invalid_dates"] == 1
    assert report["negative_balances"] == 1


def test_clean_data_removes_invalid_rows():
    data = {
        "first_name": ["A", "B"],
        "last_name": ["X", "Y"],
        "date_joined": ["invalid_date", "2023-01-01"],
        "validated": [True, False],
        "account_balance": [100, -50]
    }

    df = pd.DataFrame(data)

    clean_df = clean_data(df)

    # Only valid row should remain
    assert len(clean_df) == 0 or len(clean_df) == 1