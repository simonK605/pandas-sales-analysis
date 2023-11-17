import pandas as pd
import os

all_months_data = pd.DataFrame()

# Get the list of files
files = [file for file in os.listdir("./sales-data")]
for file in files:
    df = pd.read_csv("./sales-data/" + file)
    all_months_data = pd.concat([all_months_data, df])

# Export data to csv
all_months_data.to_csv("all_data.csv", index=False)
all_data = pd.read_csv("all_data.csv")