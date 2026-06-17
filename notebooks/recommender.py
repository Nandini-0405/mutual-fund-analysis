import os
import pandas as pd

# Set Project Path
os.chdir(r"C:\Users\nandi\OneDrive\Desktop\mutual_fund_analysis")

# Load Data
perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

# User Input
risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
)

# Filter Funds
result = (
    perf[
        perf["risk_grade"]
        .str.lower()
        ==
        risk.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

# Output
print("\nTop 3 Recommended Funds:\n")

print(
    result[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)