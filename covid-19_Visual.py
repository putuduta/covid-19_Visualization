import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'D:\Covid-19 - Visualization\Data\Case by Provinces - IDN-COVID19 - Sheet2.csv')

columns = ['Type', 'Features Type', 'ID-number', 'Province_code', 'Features Geometry Type', 'Features Geometry Coordinates']
df = df.drop(columns, axis = 1)

# Sorting Based on Confirmed Cases and Death cases
top_provinces = df.sort_values(["Confirmed_cases", "Death_cases"], ascending = [False, False])
# print(top_provinces)

# # In the first five Provinces
Province_names = top_provinces['Province_name'].head()
Confirmed_cases = top_provinces['Confirmed_cases'].head()
Death_cases = top_provinces['Death_cases'].head()
Recovered_cases = top_provinces['Recovered_cases'].head()

# # All provinces
# Province_names = df['Province_name']
# Confirmed_cases = df['Confirmed_cases']
# Death_cases = df['Death_cases']
# Recovered_cases = df['Recovered_cases']

# # Using scatter plot bnsed on confirmed case and death cases
# plt.scatter(x = Confirmed_cases, y = Death_cases)
# plt.xscale("log")
# plt.xlabel('Confirmed Cases')
# plt.ylabel('Death Cases')
# plt.title('COVID-19 Cases')
# plt.show()

# Using bar chart
y_pos = np.arange(len(Province_names))

plt.bar(y_pos + 0, Confirmed_cases, width = 0.2, color = 'navy', label = 'Confirmed Cases')
plt.bar(y_pos + 0.2, Recovered_cases, width = 0.2, color = 'darkcyan', label = 'Recovered Cases')
plt.bar(y_pos + 0.4, Death_cases, width = 0.2, color = 'skyblue', label = 'Death Cases')

plt.xticks(y_pos, Province_names)
plt.xlabel('Province Names')
plt.ylabel('Cases')
plt.legend(('Confirmed Cases', 'Recovered Cases', 'Death Cases'))
plt.title('COVID-19 Cases')
plt.show()
