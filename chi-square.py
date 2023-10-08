import pandas as pd 
from scipy.stats import chi2_contingency

df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_5_statistics/main/datasets/1c59b26a-1684-4bfb-92f7-205b947530cf.csv.csv')

df['sex'].value_counts()
df['combined_od1'].value_counts()

contingency_table = pd.crosstab(df['combined_od1'], df['sex'])
print(contingency_table)

chi2, p, _, _ = chi2_contingency(contingency_table)
print(f"Chi2 value: {chi2}")
print(f"P-value: {p}")