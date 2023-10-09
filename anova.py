import pandas as pd
import scipy.stats as stats

# Upload the CSV file 
df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_5_statistics/main/datasets/TMEDTREND_PUBLIC_230821.csv')

# Filter out rows where 'Bene_Geo_Desc' is not null
filtered_df = df.dropna(subset=['Bene_Geo_Desc'])

# Perform ANOVA
f_statistic, p_value = stats.f_oneway(
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Alabama']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Alaska']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Arizona']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Arkansas']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'California']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Colorado']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Connecticut']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Delaware']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'District Of Columbia']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Florida']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Georgia']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Hawaii']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Idaho']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Illinois']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Indiana']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Iowa']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Kansas']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Kentucky']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Louisiana']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Maine']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Maryland']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Massachusetts']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Michigan']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Minnesota']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Mississippi']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Missouri']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Montana']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'National']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Nebraska']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Nevada']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'New Hampshire']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'New Jersey']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'New Mexico']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'New York']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'North Carolina']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'North Dakota']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Ohio']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Oklahoma']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Oregon']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Pennsylvania']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Puerto Rico']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Rhode Island']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'South Carolina']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'South Dakota']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Tennessee']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Territories']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Texas']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Utah']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Vermont']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Virgin Islands']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Virginia']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Washington']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'West Virginia']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Wisconsin']['Total_Bene_Telehealth'],
    filtered_df[filtered_df['Bene_Geo_Desc'] == 'Wyoming']['Total_Bene_Telehealth'],
)

# Define significance level (alpha)
alpha = 0.05

# Check p-value against alpha
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in telehealth usage among geographic locations.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in telehealth usage among geographic locations.")

# Print the F-statistic and p-value
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")
