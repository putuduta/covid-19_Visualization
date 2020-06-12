import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'D:\Covid-19 - Visualization\Data\data-penambahan-kasus-covid-19-bulan-mei-tahun-2020.csv')

# print(df.tail())

# selama tanggal 27 - 31 bulan mei
sns.relplot(x = 'tanggal', y = 'jumlah', data = df.tail(15), kind = 'line', style = 'diagnosa', hue = 'diagnosa', ci = None)

plt.show()