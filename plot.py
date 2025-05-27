import matplotlib.pyplot as plt
import pandas as pd

fname = 'pollen_counts.csv'
data = pd.read_csv(fname)

step = len(data) // 5

plt.plot(data.date, data['count'])
plt.xticks(data.date[::step], rotation=45)
plt.show()
