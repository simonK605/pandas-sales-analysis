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

# Find NAN
nan_df = all_data[all_data.isna().any(axis=1)]

# Drop NAN
all_data = all_data.dropna(how='all')

# Find 'Or' because of wrong data (Order Date)
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# Fix dtype
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')