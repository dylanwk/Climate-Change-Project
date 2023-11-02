import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the path to your CSV file.
file_path = 'polar_ice_levels.csv'

# Read the CSV file into a pandas DataFrame.
df = pd.read_csv(file_path, delimiter=',', skipinitialspace=True)

sqkm_to_sqmiles = 0.239913
df['(1) Northern_Hemisphere'] = df['(1) Northern_Hemisphere']

# Filter the DataFrame to select rows with specific 'Date' values.
target_dates = range(2017001, 2024001, 1000)  # This generates a list of target dates.
filtered_df = df[df['(0) Date'].isin(target_dates)]

# Set 'Date' column as the index.
df.set_index('(0) Date', inplace=True)

# Select the columns you want to plot.
columns_to_plot = [
    '(1) Northern_Hemisphere'
]

# Create a line plot for the selected columns.
ax = filtered_df[columns_to_plot].plot(legend=True, figsize=(12, 6))

# Add labels and a title to the plot.
plt.xlabel('Year')
plt.ylabel('Ice Extent (Sq. Miles)')
plt.title('Sea Ice Extent Over Time (2017-2023)')

# Set custom x-axis labels
new_x_labels = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
ax.set_xticklabels(new_x_labels)

# Show the plot.
plt.show()







