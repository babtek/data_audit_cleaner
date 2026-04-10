import os
import logging


def load_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    logging.info(f"Clean data written to {output_path}")


def save_report(report, report_path):
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        f.write(str(report))
    logging.info(f"Report saved to {report_path}")

