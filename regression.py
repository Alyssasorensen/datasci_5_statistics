import pandas as pd 
import statsmodels.api as sm
import matplotlib.pyplot as plt

# load in dataset
df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_5_statistics/main/datasets/Stroke_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County___2018-2020.csv')

df.columns

## vars of interest: Data Value and Latitude
df = df[['Data_Value', 'Y_lat']]

# Remove any row with missing data
df = df.dropna()

# lets remove outliers, greater then 3 SDs from the mean
df = df[(df['Data_Value'] - df['Data_Value'].mean()) / df['Data_Value'].std() < 3]
df = df[(df['Y_lat'] - df['Y_lat'].mean()) / df['Y_lat'].std() < 3]
df

df.head(20)

# save 
df.to_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_5_statistics/main/datasets/Stroke_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County___2018-2020.csv')

# Define the dependent and independent variables
X = df['Data_Value']
y = df['Y_lat']

# Add a constant to the independent variable (required for the statsmodels regression model)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression
print(model.summary())

plt.scatter(df['Data_Value'], df['Y_lat'], label='Data Points')
plt.plot(df['Data_Value'], model.predict(X), color='red', label='Regression Line')
plt.xlabel('Data_Value')
plt.ylabel('Y_lat')
plt.title('Relationship Between Data Value and Latitude')
plt.legend()
plt.show()