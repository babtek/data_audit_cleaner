import os
import pandas as pd
import pytest

from src.extract import extract_data


def test_extract_data_success(tmp_path):
    # Create a temporary CSV file
    file_path = tmp_path / "test.csv"

    df = pd.DataFrame({
        "first_name": ["John"],
        "last_name": ["Smith"],
        "date_joined": ["2023-01-01"],
        "validated": [True],
        "account_balance": [100.0]
    })

    df.to_csv(file_path, index=False)

    result = extract_data(file_path)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert list(result.columns) == list(df.columns)


def test_extract_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        extract_data("non_existent_file.csv")


def test_extract_data_empty_file(tmp_path):
    file_path = tmp_path / "empty.csv"

    # Create empty file
    file_path.write_text("")

    with pytest.raises(pd.errors.EmptyDataError):
        extract_data(file_path)


def test_extract_data_malformed_csv(tmp_path):
    file_path = tmp_path / "bad.csv"

    # Write malformed CSV content
    file_path.write_text("first_name,last_name\nJohn")

    # Pandas may still parse this, so we check structure instead
    df = extract_data(file_path)

    assert "first_name" in df.columns