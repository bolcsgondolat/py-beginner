# Import libraries and packages
import pandas as pd
import matplotlib.pyplot as plt
# RUN THIS CELL TO IMPORT YOUR DATA.
companies = pd.read_csv("Unicorn_Companies.csv")
# Display the first 10 rows of the data
companies.head()
# How large the dataset is
companies.size
#It has 10740 cells which makes it quite large.
# Shape of the dataset
companies.shape
#It stores 10 types of information on 1074 companies.
# Get information
companies.info()
# Get descriptive statistics
companies.describe()
# Use pd.to_datetime() to convert Date Joined column to datetime & update the column with the converted values
companies['Date Joined'] = pd.to_datetime(companies['Date Joined'])
# Use .info() to confirm that the update actually took place
companies.info()
# Use .dt.year to extract year component from Date Joined column & add the result as a new column named Year Joined to the DataFrame
companies['Year Joined'] = companies['Date Joined'].dt.year
# Use .head() to confirm that the new column did get added
companies.head()
# Sample the data
companies_sampled = companies.sample(n=50, random_state=1)
companies_sampled
# Prepare data for plotting
companies_sampled['Status Reach Time'] = companies_sampled['Year Joined'] - companies_sampled['Year Founded']
max_status_reach_time = companies_sampled.groupby('Industry')['Status Reach Time'].max().reset_index()
max_status_reach_time
# Create bar plot
# with the various industries as the categories of the bars
# and the time it took to reach unicorn status as the height of the bars
max_status_reach_time = max_status_reach_time.sort_values(by='Status Reach Time', ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(max_status_reach_time['Industry'], max_status_reach_time['Status Reach Time'])
# Set title
plt.title("Time to Reach Unicorn Status by Industry")
# Set x-axis label
plt.xlabel("Industry")
# Set y-axis label
plt.ylabel("Time to Reach Unicorn Status (Years)")
# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text
plt.xticks(rotation=90)
# Display the plot
plt.show()
# Create a column representing company valuation as numeric data
max_valuation = companies_sampled.groupby('Industry')['Valuation'].max().reset_index()
max_valuation
# Create bar plot
# with the various industries as the categories of the bars
# and the maximum valuation for each industry as the height of the bars
max_valuation = max_valuation.sort_values(by='Valuation', ascending=True)
plt.figure(figsize=(10, 6))
plt.bar(max_valuation['Industry'], max_valuation['Valuation'])
# Set title
plt.title("Maximum Valuation by Industry")
# Set x-axis label
plt.xlabel("Industry")
# Set y-axis label
plt.ylabel("Maximum Valuation")
# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text
plt.xticks(rotation=90)
# Display the plot
plt.show()