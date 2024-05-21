# Import the relevant Python libraries and modules needed in this lab.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# RUN THIS CELL TO IMPORT YOUR DATA.
companies = pd.read_csv("Unicorn_Companies.csv")
# Display the first 10 rows of the data.
companies.head(10)
# Identify the number of rows and columns in the dataset.
companies.shape
# Check for duplicates.
companies.drop_duplicates().shape
# Display the data types of the columns.
companies.info()
#companies.info
# Sort `companies` and display the first 10 rows of the resulting DataFrame.
companies.sort_values(by="Year Founded", ascending=True, inplace=True)
companies
# Display each unique year that occurs in the dataset along with the number of companies that were founded in each unique year.
companies["Year Founded"].value_counts
# Plot a histogram of the Year Founded feature.
sns.histplot(data=companies, x="Year Founded")
plt.show()
# Convert the `Date Joined` column to datetime. Update the column with the converted values.
companies["Date Joined"] = pd.to_datetime(companies["Date Joined"])
# Display the data types of the columns in `companies` to confirm the update.
companies.dtypes
# Obtain the names of the months when companies gained unicorn status. Use the result to create a `Month Joined` column.
companies['Month Joined'] = companies['Date Joined'].dt.month
# Display the first few rows of `companies` to confirm that the new column did get added.
companies.head()
# Determine how many years it took for companies to reach unicorn status. Use the result to create a `Years To Join` column.
companies['Years To Join'] = companies['Date Joined'].dt.year - companies['Year Founded']
# Display the first few rows of `companies` to confirm that the new column did get added.
companies.head()
# After identifying the time interval that interests you, proceed with the following:
# Step 1. Take the subset that you defined for the year of interest. 
#         Insert a column that contains the time interval that each data point belongs to, as needed.
subset_2010 = companies.query("`Year Founded` >= 2000 and `Year Founded` < 2010")
subset_2010["Date Joined"] = pd.to_datetime(subset_2010["Date Joined"])
subset_2010["quarter"] = subset_2010["Date Joined"].dt.quarter
# Step 2. Group by the time interval.
#         Aggregate by counting companies that joined per interval of that year.
#         Save the resulting DataFrame in a new variable.
trends_2010 = subset_2010.groupby("quarter").agg(count=("Company", "count"))
# Display the first few rows of the new DataFrame to confirm that it was created
trends_2010.head()
# Ensure all values in 'Valuation' are treated as strings
companies['Valuation'] = companies['Valuation'].astype(str)
# Remove non-numeric characters from the 'Valuation' column and convert to numeric
companies['Valuation'] = companies['Valuation'].str.replace('[\$,B]', '', regex=True).astype(float)
# Filter the data for the years of interest
subset_2015 = companies[companies["Year Joined"] == 2015]
subset_2020 = companies[companies["Year Joined"] == 2020]
# Concatenate the two subsets
concatenated_companies = pd.concat([subset_2015, subset_2020])
# Add a column for the time interval
concatenated_companies["Years To Join"] = concatenated_companies["Year Joined"] - concatenated_companies["Year Founded"]
# Add a column indicating the year of joining
concatenated_companies["Join Year"] = concatenated_companies["Year Joined"]
# Group by the time interval and join year, then compute the average valuation
result = concatenated_companies.groupby(["Years To Join", "Join Year"]).agg(AverageValuation=pd.NamedAgg(column="Valuation", aggfunc="mean")).reset_index()
# Plot the trends
plt.figure(figsize=(10, 6))
# Plot for the year 2015
plt.plot(result[result["Join Year"] == 2015]["Years To Join"], result[result["Join Year"] == 2015]["AverageValuation"], label="2015", marker='o')
# Plot for the year 2020
plt.plot(result[result["Join Year"] == 2020]["Years To Join"], result[result["Join Year"] == 2020]["AverageValuation"], label="2020", marker='o')
# Set title and labels
plt.title("Average Valuation of Companies Becoming Unicorns Over Time")
plt.xlabel("Years to Join")
plt.ylabel("Average Valuation (in billions)")
# Add legend
plt.legend()
# Show plot
plt.show()