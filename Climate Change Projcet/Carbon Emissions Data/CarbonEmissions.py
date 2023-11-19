
import pandas as pd
import matplotlib.pyplot as plt

""" 
-- Carbon Emission Graph -- date finished 11/19

Read user input from the terminal as the country to plot.
Using this variable and the co2 data file, plot the total co2 emissions
of that country 

"""

df = pd.read_csv("owid-co2-data.csv")

country_to_plot = str(input("Enter a Country (Capatalized): "))

filtered_df = df[df['country'] == country_to_plot]


plt.plot(filtered_df['year'], filtered_df['co2'], marker='', linestyle='-', color='b', label=country_to_plot)



plt.xlabel('Year')
plt.ylabel('CO2 (in million tonnes)')
plt.title(f'Annual total emissions of carbon dioxide (CO₂) in {country_to_plot}')
plt.legend()  # legend of country name


plt.show()