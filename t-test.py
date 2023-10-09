import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind

# Read in the data
df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_5_statistics/main/datasets/COVID-19_Cases_and_Deaths_by_Age_Group_-_ARCHIVE.csv') 
len(df)

## keep only complete rows
df = df.dropna()
len(df)

# Separate the data for the two age groups
age_group_0_9 = df[df['AgeGroups'] == '0-9']
df

age_group_80_and_older = df[df['AgeGroups'] == '80 and older']
df

# Extract the 'Total deaths' columns for both age groups
deaths_0_9 = age_group_0_9['Total deaths']
deaths_0_9 

deaths_80_and_older = age_group_80_and_older['Total deaths']
deaths_80_and_older

# Perform a two-sample t-test
t_statistic, p_value = stats.ttest_ind(deaths_0_9, deaths_80_and_older)
t_statistic, p_value

# Set the significance level (alpha)
alpha = 0.05

# Print the results
print(f'T-statistic: {t_statistic}')
print(f'P-value: {p_value}')

# Determine whether to reject the null hypothesis
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in total deaths.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in total deaths.")
