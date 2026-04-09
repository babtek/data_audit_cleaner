import pandas as pd

def audit_data(df):
    report = {}

    report["rows"] = len(df)
    report["duplicates"] = df.duplicated().sum()
    report["missing_values"] = df.isnull().sum().to_dict()

    return report

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def main():
    df = pd.read_csv("data/sample.csv")

    report = audit_data(df)
    print("Audit Report:", report)

    clean_df = clean_data(df)
    clean_df.to_csv("reports/cleaned.csv", index=False)

    with open("reports/report.txt", "w") as f:
        f.write(str(report))

if __name__ == "__main__":
    main()