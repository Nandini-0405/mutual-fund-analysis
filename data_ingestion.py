import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        print("\n" + "="*60)
        print("FILE:", file)

        df = pd.read_csv(os.path.join(folder, file))

        print("Shape:", df.shape)
        print("\nDtypes:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())