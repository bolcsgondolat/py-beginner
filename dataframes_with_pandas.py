import numpy as np
import pandas as pd
#Read in the first file
top3 = pd.read_csv('epa_ca_tx_pa.csv')
top3.head(5)
#Metadata
top3.info()
#Summary statistics
top3.describe()
#Rows per state
top3["state_name"].value_counts()
#Sort by AQI
top3_sorted = top3.sort_values(by="aqi", axis=0, ascending=False)
print(top3_sorted.head(n=10))
#Use iloc to select rows
top3_sorted.iloc[[10, 11]]
# Create a boolean mask to select observations from California
mask = top3_sorted['state_name'] == 'California'
# Apply the boolean mask to the top3_sorted DataFrame
ca_df = top3_sorted[mask]
# Print the first five rows of ca_df
print(ca_df.head())
#Validate ca_df data
ca_df.shape
#Rows per CA county
ca_df.county_name.value_counts()
#mean aqi for LA
mask = ca_df["county_name"] == "Los Angeles"
filtered_ca_df = ca_df[mask]
filtered_ca_df.aqi.mean()
#groupby
top3.groupby("state_name").mean()['aqi']
#read in second file
other_states = pd.read_csv("epa_others.csv")
other_states.head(n=5)
#Concatenate the data
combined_df = pd.concat([top3, other_states], axis=0, join='outer')
len(combined_df) == len(top3) + len(other_states)
#Complex boolean masking
mask = (combined_df["state_name"] == "Washington") & (combined_df["aqi"] >= 51)
combined_df[mask]