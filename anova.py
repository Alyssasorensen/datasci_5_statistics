import pandas as pd
import scipy.stats as stats

# Upload the CSV file 
df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_5_statistics/main/datasets/COVID-19_Hospital_Capacity.csv')

# Perform ANOVA
f_statistic, p_value = stats.f_oneway(
    df[df['Bed Type'] == 'Intensive Care']['Count'],
    df[df['Bed Type'] == 'Acute Care']['Count'],
    df[df['Bed Type'] == 'Acute Care Surge']['Count'],
)

# Define significance level (alpha)
alpha = 0.05

# Check p-value against alpha
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in patient counts among bed types.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in patient counts among bed types.")

# Print the F-statistic and p-value
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")
