import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv(r'D:\Covid-19 - Visualization\Data\Daily-Update IDN-COVID19 - Sheet5.csv')


# Cleaning the data
columns = ['Cumulative_cases', 'Recovered_cases', 'Total_death', 'Patient_under_treatment', 'Treatment_cases_perDay']
df = df.drop(columns, axis = 1)

# print(df)

sns.relplot(x='Date', y='Recovered-cases_perDay', data=df.tail(), kind='line', label='Recoverd Cases')
sns.relplot(x='Date', y='New_case_per_day', data=df.tail(), kind='line', color='olive', label='New Cases')
sns.relplot(x='Date', y='Death_cases_perDay', data=df.tail(), kind='line', linestyle='dashed', label='Death Cases')

plt.legend()

plt.show()