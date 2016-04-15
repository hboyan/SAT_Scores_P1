#Author: Haley Boyan
#NumPy Lab
#reshape an array

import numpy as np

#Create an array
#array1 = np.random.randint(0,high=10,size=(6,6))
array1 = np.arange(36).reshape(6,6)
print "Original array (6x6): "
print array1
print

#Reshape the array to 2x6 and 1x12
print "As 4x9 array: "
print np.reshape(array1,[4,9])
print

print "As 1x36 array: "
print np.reshape(array1,[1,36])
print

#Transpose the array
print "Transposed: "
print np.transpose(array1)
print

#Bonus:Different ways to index the array (6)
print "Other indexing methods: "
print "Slicing uses format [start(inclusive):stop(exclusive):step], with defaults [begining:end:1]"
print "1: x[1:3]"
print array1[1:3]
print "2: x[:-4]"
print array1[:-4]
print "3: x[1:5:2]"
print array1[1:5:2]
print "4: x[::]"
print array1[::]
print "5: x[1::2,:5:3] (first slices from index 1 to end with steps of 2, then slices the result from beginning to index 5 in steps of 3)"
print array1[1::2,:5:3]
