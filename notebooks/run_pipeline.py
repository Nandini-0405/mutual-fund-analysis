"""
Bluestock Mutual Fund Analytics Dashboard
Master Pipeline Script

This script executes the complete project workflow.
"""

import subprocess
import os

# Project Path
os.chdir(r"C:\Users\nandi\OneDrive\Desktop\mutual_fund_analysis")

print("=" * 50)
print("BLUESTOCK MUTUAL FUND PROJECT PIPELINE")
print("=" * 50)

scripts = [
    "data_ingestion.py",
    "clean_nav_history.py",
    "clean_investor_transactions.py",
    "load_to_sqlite.py",
    "live_nav_fetch.py"
]

for script in scripts:
    if os.path.exists(script):
        print(f"\nRunning {script}...")
        subprocess.run(["python", script])
    else:
        print(f"\nSkipping {script} (File not found)")

print("\nPipeline Execution Completed Successfully!")