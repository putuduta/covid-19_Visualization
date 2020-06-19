import pandas as pd
import numpy as np
import plotly.express as px

# Read the data
data = pd.read_csv(r'D:\Covid-19 - Visualization\Data\covid_19_clean_complete.csv')
df = pd.DataFrame(data)

# Rename column
df = df.rename(columns={'Country/Region': 'Country'})

# # Select the country you want to find
# start_date = input("Select a start date in mm/dd/yy format: ")
# end_date = input("Select a start date in mm/dd/yy format: ")
# country = input("Select a country: ")
# df['Date'] = pd.to_datetime(df['Date'])
# date_range_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
# country_date_range_df = date_range_df[date_range_df['Country'] == country]
# # print(country_date_range_df)

# graph = px.line(country_date_range_df, title = "Number of confirmed Covid-19 Cases",x = "Date", y = "Confirmed")

# Multiple Country
start_date = input("Select a start date in mm/dd/yy format: ")
end_date = input("Select a start date in mm/dd/yy format: ")
country = input("Select countries, separated by commas: ")
country_list = country.split(',')
df['Date'] = pd.to_datetime(df['Date'])
date_range_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
country_date_range_df = date_range_df[date_range_df.Country.isin(country_list)]
country_date_range_df

graph = px.line(country_date_range_df, title = "Number of confirmed Covid-19 Cases by Country",x = "Date", y = "Confirmed", color='Country')


graph.show()