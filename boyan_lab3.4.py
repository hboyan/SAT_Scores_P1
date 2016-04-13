#Author: Haley Boyan
#Lab 3.4
import numpy

#Create a list
numlist = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,6.8,
12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,25.3,31.6,27.3,33.0,
32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

def numpytime(list):
    #Find the mean of the list
    print("mean: " + str(numpy.mean(numlist)))
    #Find the median of the list
    print("median: " +str(numpy.median(numlist)))
    #Find the variance of the list
    print("variance: " +str(numpy.var(numlist)))
    #Find the standard deviation of the list
    print("standard deviation: " +str(numpy.std(numlist)))

    #Bonus: Replace a value in the list
    numlist[0] = 100

numpytime(numlist)
