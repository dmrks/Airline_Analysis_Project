import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1 = About normally distributed about a mean price of 370 - High Values = Beyond 500, Low Values = Less than 250 - 500 Dollar is pricy for a ticket
plt.hist(flight.coach_price)
plt.show() # Show the plot
plt.clf() # Clear the plot

sns.boxplot(flight.coach_price)
plt.show() # Show the plot
plt.clf() # Clear the plot

## Task 2 AVG = 431.834377372817, Median = 437.115 -> Still overpriced
print(np.mean(flight.coach_price[flight.hours == 8 ]))
print(np.median(flight.coach_price[flight.hours == 8 ]))

plt.hist(flight.coach_price[flight.hours ==8 ])
plt.show() # Show the plot
plt.clf() # Clear the plot

## Task 3 on AVG 13.162844814301126 (Median 10.0) Delay on Flight
print(np.mean(flight.delay))
print(np.median(flight.delay))

plt.hist(flight.delay[flight.delay<= 10])
plt.show() # Show the plot
plt.clf() # Clear the plot

plt.hist(flight.delay[flight.delay>= 10])
plt.show() # Show the plot
plt.clf() # Clear the plot

## Task 4 = Flights with higher coach prices have usually higher first-class prices (Pearson = .758)

plt.scatter(flight.coach_price, flight.firstclass_price)
plt.show() # Show the plot
plt.clf() # Clear the plot

pearson =np.corrcoef(flight.coach_price,flight.firstclass_price)
print(pearson)

## Task 5 Mean Difference in Coachprice regarding a Inflight_Meal is small, Entertainment or Wifi is signifficantly higher

sns.boxplot(x = flight.coach_price, y = flight.inflight_meal, palette = "pastel")
plt.show() # Show the plot
plt.clf() # Clear the plot

sns.boxplot(x = flight.coach_price, y = flight.inflight_entertainment, palette = "pastel")
plt.show() # Show the plot
plt.clf() # Clear the plot

sns.boxplot(x = flight.coach_price, y = flight.inflight_wifi, palette = "pastel")

plt.show() # Show the plot
plt.clf() # Clear the plot

## Task 6 = break in the distribution of passengers around 180 (very few flights have around 180 passengers), Less Passengers on 6 and 8 Hour flights

perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))

sns.lmplot(x = "hours", y = "passengers", data = flight_sub, x_jitter = 0.25, scatter_kws={"s": 5, "alpha":0.2}, fit_reg = False)

plt.show() # Show the plot
plt.clf() # Clear the plot

## Task 7 = Flying on the weekends is more expensive then in the week
sns.lmplot(x ='coach_price', y='firstclass_price', hue = 'weekend', data = flight_sub, fit_reg= False)
plt.show()
plt.clf()
 
 
## Task 8 = Flying on the weekends is more expensive then in the week
sns.boxplot(x = "day_of_week", y = "coach_price", hue = "redeye", data = flight)
plt.show()
plt.clf()





