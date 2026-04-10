import logging
import pandas as pd

def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Extracted {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Failed to extract data: {e}")
        raise