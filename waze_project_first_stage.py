# Import packages for data manipulation
import pandas as pd
import numpy as np
# Load dataset into dataframe
df = pd.read_csv('waze_dataset.csv')
#View and inspect summary information
df.head(10)
df.info()
#Data types include floats, integers and objects. It has 14,999 rows and 13 columns.
#700 users have no labels. Isolate rows with null values.
null_mask = df.isnull().any(axis=1)
null_rows = df[null_mask]
# Display summary stats of rows with null values
null_rows
# Isolate rows without null values
not_null_mask = df.notnull().all(axis=1)
not_null_rows = df[not_null_mask]
# Display summary stats of rows without null values
not_null_rows
#Aside from the missing labels, there are not really any obvious differences.
# Get count of null values by device (null values are represented by NaN)
# Filter null rows by device type
null_rows = df[df['label'].isnull()]

# Count null values for each device
null_android_count = null_rows[null_rows['device'] == 'Android'].shape[0]
null_iphone_count = null_rows[null_rows['device'] == 'iPhone'].shape[0]
print("Count of null values for Android devices:", null_android_count)
print("Count of null values for iPhone devices:", null_iphone_count)
#There were 253 Android users, and 447 Iphone users who had null values.

# Calculate % of iPhone nulls and Android nulls
# Calculate total count of null values
total_null_count = null_rows.shape[0]
# Count null values for each device
null_android_count = null_rows[null_rows['device'] == 'Android'].shape[0]
null_iphone_count = null_rows[null_rows['device'] == 'iPhone'].shape[0]
# Calculate percentage of null values for each device
percentage_null_android = (null_android_count / total_null_count) * 100
percentage_null_iphone = (null_iphone_count / total_null_count) * 100
print("Percentage of null values for Android devices:", percentage_null_android)
print("Percentage of null values for iPhone devices:", percentage_null_iphone)

# Calculate % of iPhone users and Android users in full dataset
# Count values for each device
android_count = df[df['device'] == 'Android'].shape[0]
iphone_count = df[df['device'] == 'iPhone'].shape[0]
print("Count of Android devices:", android_count)
print("Count of iPhone devices:", iphone_count)

# Calculate % of iPhone users and Android users in full dataset
# Count values for each device
android_count = df[df['device'] == 'Android'].shape[0]
iphone_count = df[df['device'] == 'iPhone'].shape[0]
# Calculate total count of entries in the dataset
total_count = df.shape[0]
# Calculate percentage of Android and iPhone users
percentage_android = (android_count / total_count) * 100
percentage_iphone = (iphone_count / total_count) * 100
print("Percentage of values for Android devices:", percentage_android)
print("Percentage of values for iPhone devices:", percentage_iphone)
#The percentage of missing values by each device is consistent with their representation in the data overall. 
#There is nothing to suggest a non-random cause of the missing data.

# Calculate counts of churned vs. retained
churned_count = df[df['label'] == 'churned'].shape[0]
retained_count = df[df['label'] == 'retained'].shape[0]
print("Count of churned users:", churned_count)
print("Count of retained users:", retained_count)
# Calculate total count of entries in the dataset
retained_and_churned_count = churned_count + retained_count
print("Sum of users with labels:", retained_and_churned_count)
# Calculate percentages of churned and retained users
percentage_churned = (churned_count / retained_and_churned_count) * 100
percentage_retained = (retained_count / retained_and_churned_count) * 100
print("Percentage of churned users:", percentage_churned)
print("Percentage of retained users:", percentage_retained)

# Calculate median values of all columns for churned and retained users
print(df[df['label'] == 'churned'].median())
print(df[df['label'] == 'retained'].median())
#It seems that churned users had more drives in fewer days, and their trips were farther and longer in duration. Perhaps this is suggestive of a user profile.

# Add a column to df called `km_per_drive`
df['km_per_drive'] = df['driven_km_drives'] / df['drives']
# Group by `label` and calculate the median km per drive for each group
median_km_per_drive = df.groupby('label')['km_per_drive'].median()
print("Median kilometers per drive for churned users:", median_km_per_drive['churned'])
print("Median kilometers per drive for retained users:", median_km_per_drive['retained'])

# Add a column to df called `km_per_driving_day`
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']
# Group by `label`, calculate the median, and isolate for km per driving day
median_km_per_driving_day = df.groupby('label')['km_per_driving_day'].median()
print("Median kilometers per day for churned users:", median_km_per_driving_day['churned'])
print("Median kilometers per day for retained users:", median_km_per_driving_day['retained'])

# Add a column to df called `drives_per_driving_day`
df['drives_per_driving_day'] = df['drives'] / df['driving_days']
# Group by `label`, calculate the median, and isolate for drives per driving day
median_drives_per_driving_day = df.groupby('label')['drives_per_driving_day'].median()
print("Median number of drives per driving day for churned users:", median_drives_per_driving_day['churned'])
print("Median number of drives per driving day for retained users:", median_drives_per_driving_day['retained'])
#Safe to assume this data does not represent typical drivers at large. 
#Perhaps the data—and in particular the sample of churned users—contains a high proportion of long-haul truckers.

# For each label, calculate the number of Android users and iPhone users
device_counts = df.groupby(['label', 'device']).size()
device_counts
# For each label, calculate the percentage of Android users and iPhone users
# Create a pivot table to calculate percentages of Android and iPhone users within each group
pivot_table = df.pivot_table(index='label', columns='device', aggfunc='size', fill_value=0)
# Calculate total counts for churned and retained users
total_churned = pivot_table.loc['churned'].sum()
total_retained = pivot_table.loc['retained'].sum()
# Calculate percentages
percentages_churned = (pivot_table.loc['churned'] / total_churned) * 100
percentages_retained = (pivot_table.loc['retained'] / total_retained) * 100
print("Percentages of churned Android and iPhone users:", percentages_churned)
print("\nPercentages of retained Android and iPhone users:", percentages_retained)
#The ratio is consistent between the churned group and the retained group, and with those ratios found in the overall dataset.