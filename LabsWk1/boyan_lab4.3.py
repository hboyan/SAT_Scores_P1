#Author: Haley Boyan
import numpy as np

#Write a function that computes the variance
def variance(set):
    total = 0
    for x in set:
        total+=x
    mean=total/len(set)

    total = 0
    for x in set:
        total+=(x-mean)**2
    set_var = total/len(set)

    return set_var

#Write a function that computes the standard deviation
def std_dev(set):
    var = variance(set)
    std_dev = np.sqrt(var)

    return std_dev

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

#Compare your functions to the results of the numpy equivalents
print "Variance: "
print "Calculated: "+str(variance(X))
print "NumPy: "+str(np.var(X))
print
print "Standard Deviation: "
print "Calculated: "+str(std_dev(X))
print "NumPy: "+str(np.std(X))
