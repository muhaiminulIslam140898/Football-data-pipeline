import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('scripts/data/clean_data.csv', parse_dates=['date'])

# Example plot
sns.histplot(df['home_score'], bins=range(0, 10), kde=False)
plt.title('Distribution of Home Team Goals')
plt.xlabel('Goals')
plt.ylabel('Matches')
plt.show()