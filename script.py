# Import modules
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

# Save featured games as games
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

# Save number of viewers per each featured game as viewers
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# Plot a bar graph
plt.bar(range(len(games)), viewers, color='darkblue')

# Add title
plt.title('Featured Games Viewers')

# Add legend
plt.legend(['Twitch'])

# Add x-axis lebel
plt.xlabel('Games')

# Add y-axis
plt.ylabel('Viewers')

# Create an axis object as ax
ax = plt.subplot()

# Set x-ticks
ax.set_xticks(range(11))

# Set x-tick labels
ax.set_xticklabels(games, rotation=30)

# Show plot
plt.show()

# Pie Chart: League of Legends Viewers' Whereabouts

# list of country names
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

# List of views per each country
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

# Create list of colors as colors
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

# Clear current figure
plt.clf()

# Create break out points as explode
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Plot a pie chart
plt.pie(countries, explode=explode, colors=colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)

# Add title
plt.title("League of Legends Viewers' Whereabout")

# Add legends
plt.legend(labels, loc='right')

# Show plot
plt.show()

# Line Graph: Time Series Analysis

# Create a range of numbers (hours) from 0 to 23 (inclusive)
hour = range(24)

# Create a list of time in number of hours as viewers_hour
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

# Clear current figure
plt.clf()

# Plot a line graph
plt.plot(hour, viewers_hour)

# Add title
plt.title('Time Series')

# Add x-label
plt.xlabel('Hour')

# Add y-label
plt.ylabel('Viewers')

# Add legend
plt.legend(['2015-01-01'])

# Create an axis object as ax
ax = plt.subplot()

# Set x-ticks
ax.set_xticks(hour)

# Set y-ticks
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])

# Create a list containing the upper bound of the viewers_hour and call it y_upper
# Set the top of the shared area
y_upper = [i + (i*0.15) for i in viewers_hour]

# Create a list containing the lower bound of the viewers_hour and call it y_lower
# Set the bottom of the shared area
y_lower = [i - (i*0.15) for i in viewers_hour]

# Shade error
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)
# Show plot
plt.show()