#Haley Boyan
#Review Problem 2
#function that operates on a dictionary and a list of numbers.

#Accepts a dictionary as its first argument. The values of the dictionary should be a list of numbers.
#Accepts an optional keyword argument that is a list.
#The default should be an empty list. The optional keyword list should be called remainder.

def dictnums(dict,numlist=[]):
    #If the list is empty: append a 2 to the list.
    if numlist == []:
        numlist.append(2)

    #Print the dictionary as well as the optional list.
    print "dictionary: "
    print dict
    print "number list: "
    print numlist
    print

    #Iterate though they key:value pairs in the dictionary:
    for x in dict:
        print x + ": "
        for y in numlist:
            print x%y
        #For each value list of numbers, calculate the remainder of each number
        #for each number in the remainder list
        #for y in numlist:
            #rem = x%y
            #sys.stdout.write(rem)

#Create a dictionary where they keys are the numbers in the value list, and the values are the remainders of that number from the remainder list.
#ex: if value list == [10,9] and remainder == [2,3], the new dictionary would be: {10:[0, 1], 9:[1, 0]}
#For the current key in the dictionary entered into the function, change the value to the new remainder dictionary.
#Print out the new dictionary.
#Return the dictionary.

test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]

# 1. Run the function with the default keyword argument
dictnums(test_dict)
# 2. Run the function assigning the default keyword argument to the optional list
dictnums(test_dict,optional_remainder)
