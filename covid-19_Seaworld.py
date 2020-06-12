import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'D:\Covid-19 - Visualization\Data\Case by Provinces - IDN-COVID19 - Sheet2.csv')

columns = ['Type', 'Features Type', 'ID-number', 'Province_code', 'Features Geometry Type', 'Features Geometry Coordinates']
df = df.drop(columns, axis = 1)

# print(df.describe())

# Sorting Based on Confirmed Cases and Death cases
top_provinces = df.sort_values(["Confirmed_cases", "Death_cases"], ascending = [False, False])
# print(top_provinces)

# In the first five Provinces
Province_names = top_provinces['Province_name'].head(10)
Confirmed_cases = top_provinces['Confirmed_cases'].head(10)
Death_cases = top_provinces['Death_cases'].head(10)
Recovered_cases = top_provinces['Recovered_cases'].head(10)

# # All provinces
# Province_names = df['Province_name']
# Confirmed_cases = df['Confirmed_cases']
# Death_cases = df['Death_cases']
# Recovered_cases = df['Recovered_cases']


plt.figure(figsize = (14, 6))

plt.title('COVID-19 confirmed cases')

# showing based on confirmed cases
sns.barplot(data = top_provinces, x = Province_names, y = Confirmed_cases)
plt.ylabel('Confirmed Cases')
plt.xlabel('Province Names')

# # showing base on death cases
# sns.barplot(data = top_provinces, x = Province_names, y = Death_cases)
# plt.ylabel('Death Cases')
# plt.xlabel('Province Names')

# # Using seaborn bar plot
# sns.catplot(x = 'Province_name', y = 'Death_cases', data = top_provinces.head(), kind = 'bar')




plt.show()