import numpy as np

taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', dtype=int, skip_header=True)

#calculate mean speed of all rides
speed = np.where(taxi[:, 8] != 0, taxi[:, 7] / (taxi[:, 8] / 3600), 0) 
mean_speed = speed.mean()
print(mean_speed)

#number of rides taken in Feb month
rides_fed = taxi[taxi[:, 1 ] == 2, 1]
print(rides_fed.shape[0])

#number of rides with tip amount less than $10
print(taxi[taxi[:, -3] < 10, -3].shape[0])

#number of rides droped at JFK airport, (cords for JFK is '2')
print(taxi[taxi[:,6]==2 ,6 ].shape[0])