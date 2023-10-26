
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loaded the CSV file into a pandas DataFrame
df = pd.read_csv("GlobalLandTempuratures.csv")

# Filtered data for the United States
us_df = df[df['Country'] == 'United States']

# Extracted necessary columns (Date and Temperature)
us_df = us_df[['dt', 'AverageTemperature']]

us_df['AverageTemperature'] = (us_df['AverageTemperature'] * 9/5) + 32

# Converted the 'dt' column to a datetime object
us_df['dt'] = pd.to_datetime(us_df['dt'])

##us_df = us_df[(us_df['Year'] >= 1920 and us_df['Year'] <= 2020)]

# Grouped by year and calculate the mean temperature for each year
us_df['Year'] = us_df['dt'].dt.year
yearly_avg_temp = us_df.groupby('Year')['AverageTemperature'].mean()


# line plot
plt.figure(figsize=(12, 6))
plt.plot(yearly_avg_temp.index, yearly_avg_temp.values, marker='o', linestyle='-', color='b')
plt.title('Average Temperature in the United States Over the Years')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.grid(True)

# Show the plot
plt.show()


