import pandas as pd
import matplotlib.pyplot as plt
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

# Add 'Month' column
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

# Add 'Sales' column
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

results = all_data.groupby('Month').sum()

months = range(1, 13)
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()