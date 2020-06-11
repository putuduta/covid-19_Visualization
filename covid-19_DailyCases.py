import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'D:\Covid-19 - Visualization\Data\Daily-Update IDN-COVID19 - Sheet5.csv', index_col = "Date", parse_dates = True)

columns = ['Cumulative_cases', 'Recovered_cases', 'Total_death', 'Patient_under_treatment', 'Treatment_cases_perDay']
df = df.drop(columns, axis = 1)

# Sorting Based on new cases and recovered cases
top_cases = df.sort_values(["New_case_per_day", "Recovered-cases_perDay"], ascending = [False, False])

# print(df)

plt.title('Daily COVID-19 Cases in Indonesia')

# # showing the cases in early june
# sns.lineplot(data = df.tail())

plt.figure(figsize = (12, 6))

sns.lineplot(data = df.tail(8))

plt.show()