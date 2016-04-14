#Author: Haley Boyan
#Review problem 6 (hard)
#function that calculates the spearman correlation coefficient between two lists.
#The spearman correlation is a measure of how related two sets of numbers are.
import scipy.stats
import numpy as np

def spearman(x,y):
    print "Length of X: "+str(len(x))
    print "Length of Y: "+str(len(y))

    #Calculate the rank of the numbers in the X and Y lists.
    #Assign the rank of list X to X_rank and list Y to Y_rank
    #The rank is a number that defines what index position each number would be if the list were in order.
    #For example: say list1 = [5,2,0,9,-5], then list1_rank = [3,2,1,4,0]
    #You can use the rankdata() function from scipy.stats on a list to get the ranks of the numbers.
    X_rank = scipy.stats.rankdata(x)
    Y_rank = scipy.stats.rankdata(y)

    #Calculate the covariance between X_rank and Y_rank as XY_rank_cov:
    #The covariance is a measure of the "relatedness" between two lists of variables.

    X_mean = np.mean(X_rank) #Calculate X_mean: the mean of X_rank
    Y_mean = np.mean(Y_rank) #Calculate Y_mean: the mean of Y_rank
    X_deviation = [x-X_mean for x in X_rank] #Calculate X_deviation: subtract X_mean from each element of X_rank
    Y_deviation = [y-Y_mean for y in Y_rank] #Calculate Y_deviation: subtract Y_mean from each element of Y_rank

    #Calculate XY_d: multiply X_deviation with Y_deviation, element by element.
    XY_d = []
    for xd, yd in zip(X_deviation, Y_deviation):
        XY_d.append(xd*yd)

    sum_XY_d = np.sum(XY_d) #Calculate sum_XY_d: the sum of the elements in XY_d with np.sum()
    XY_rank_cov = sum_XY_d/len(XY_d) #Calculate XY_rank_cov: divide sum_XY_d by len(XY_d)
    #Calculate the standard deviations (X_rank_std and Y_rank_std) of the X_rank and Y_rank lists
    X_rank_std = np.std(X_rank)
    Y_rank_std = np.std(Y_rank)

    #Calculate the spearman rank correlation coefficient as XY_spearman:
    XY_spearman = XY_rank_cov/(X_rank_std * Y_rank_std)

    print "Spearman Correlation: " + str(XY_spearman)

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

#Compare your value to the scipy function for spearman: print out spearmanr(X, Y)
spearman(X,Y)
print "\nCompare to scipy calculation: "
print scipy.stats.spearmanr(X,Y)
