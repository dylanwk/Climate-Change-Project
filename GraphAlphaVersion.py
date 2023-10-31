
import pandas as pd
# import numpy as np -> not needed
import matplotlib.pyplot as plt

# Loaded the CSV file into a pandas DataFrame 10/24
df = pd.read_csv("GlobalLandTempuratures.csv")

# Filtered country value to only show United States data 10/24
us_df = df[df['Country'] == 'United States']

# Extracted Average Tempurature Value 
us_df = us_df[['dt', 'AverageTemperature']]

# Converted Average Tempurature Value from Celsius to Fahrenhiet 10/26
us_df['AverageTemperature'] = (us_df['AverageTemperature'] * 9/5) + 32

# Converted the 'dt' column to a datetime object 10/24
us_df['dt'] = pd.to_datetime(us_df['dt'])



# Grouped by year
us_df['Year'] = us_df['dt'].dt.year

# Calculated the mean temperature for each year with mean() function 10/26
yearly_avg_temp = us_df.groupby('Year')['AverageTemperature'].mean()


# Created line plot 10/26
plt.figure(figsize=(12, 6))
plt.plot(yearly_avg_temp.index, yearly_avg_temp.values, marker='o', linestyle='-', color='b')
plt.title('Average Temperature in the United States Over the Years 1920 to 2020')
plt.xlabel('Year')
plt.xlim([1920, 2020])             # Filtered year values to only the past century 10/31
plt.ylabel('Temperature (°F)')
plt.grid(True)

plt.show()


