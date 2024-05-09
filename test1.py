import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

# Read in the 2018 lightning strike dataset.
df = pd.read_csv('eda_using_basic_data_functions_in_python_dataset1.csv', nrows=10000)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Calculate days with most lightning strikes.
# Group by date and sum the number_of_strikes column
daily_strikes = df.groupby(['date']).sum()

# Sort by number of strikes in descending order
daily_strikes_sorted = daily_strikes.sort_values('number_of_strikes', ascending=False)

# Print the top 10 days with the most lightning strikes
print(daily_strikes_sorted.head(10))

# Create a new `month` column
df['month'] = df['date'].dt.month

# Calculate total number of strikes per month
monthly_strikes = df.groupby(['month']).sum()

# Sort by number of strikes in descending order
monthly_strikes_sorted = monthly_strikes.sort_values('number_of_strikes', ascending=False)

# Print the total number of strikes per month
print(monthly_strikes_sorted.head(12))
