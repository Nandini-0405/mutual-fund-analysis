import pandas as pd

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv"
]

for file in files:
    df = pd.read_csv(f"data/raw/{file}")

    print("\n" + "="*50)
    print(file)
    print("="*50)

    print(df.columns.tolist())