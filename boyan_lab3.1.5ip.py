#AWAITING LUCY FEEDBACK

#Author: Haley Boyan
#Review problem 5 (hard)
#function that calculates the pearson correlation coefficient between two lists of numbers.

#Get lists
import numpy as np

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

# Define your pearson correlation function here:
def pearsoncor(x,y):
    print ("Length of X: "+str(len(x)))
    print ("Length of Y: "+str(len(y)))
    print

    #Calculate the pearson correlation between the two lists and assign the value to variable pearson_r.
    totalx = 0
    totaly = 0
    totalxy = 0
    totalx2 = 0
    totaly2 = 0
    count = 0
    for k in range(len(x)):
        xy=x[k]*y[k]
        x2=x[k]*x[k]
        y2=y[k]*y[k]
        totalx += x[k]
        totaly += y[k]
        totalxy += xy
        totalx2 += x2
        totaly2 += y2
        count += 1
    pearson_r = ((count*totalxy) - (totalx*totaly)) / np.sqrt(((count*totalx2)-(totalx*totalx))*((count*totaly2)-(totaly*totaly)))
    print "Pearson correlation from my formula: "
    print pearson_r

    #Create a variable X_deviation that is each element of X minus the mean of X.
    x_deviation = []
    for i in range(0,len(x)-1):
        x_deviation.append(abs(x[i] - np.mean(x)))

    #Create a variable Y_deviation that is each element of Y minus the mean of Y.
    y_deviation = []
    for i in range(0,len(x)-1):
        y_deviation.append(abs(y[i] - np.mean(y)))

    #Create a variable sqrt_X_deviation_sq that is the square root
    #of the sum of the square of each element of X_deviation.
    #repeat for y
    sqrt_X_deviation_sq = np.sqrt(np.sum(x_deviation))
    sqrt_Y_deviation_sq = np.sqrt(np.sum(y_deviation))

    #Create a variable sum_XY_deviation that is the sum of each element of X and Y multiplied by
    #each other, in order. You can use the zip() function to iterate through two lists at the same time:
    sum_XY_deviation = 0
    for x_d, y_d in zip(x_deviation, y_deviation):
        combo = x_d * y_d
        sum_XY_deviation += combo

    #pearson_r is equal to sum_XY_deviation divided by (sqrt_X_deviation_sq * sqrt_Y_deviation_sq)
    pearson_r = sum_XY_deviation / (sqrt_X_deviation_sq * sqrt_Y_deviation_sq)

    print "Pearson correlation from lab instructions: "
    print pearson_r

    print "Pearson correlation from numpy: "
    #Check if it is the same as numpys correlation function.
    print np.corrcoef(x,y)[0,1]

pearsoncor(X,Y)
