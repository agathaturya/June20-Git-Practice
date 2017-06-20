""" Patient's inflammation analysis for day 1 """



import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
#Finding dimensions of data
print(data.shape)

print(data)

#Printing first row of data
print(data[0])
#aaaaaaaaaaaaaa
image-1=plt.plot(data)

#Plotting data
plt.show(image-1)