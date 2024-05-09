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