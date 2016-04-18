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
    print "original dictionary: "
    print dict
    print "remainder list: "
    print numlist
    print "remainder dictionaries for each key: "

    #Iterate though they key:value pairs in the dictionary:
    #For each value (list of numbers), calculate the remainder of each number for each number in the remainder list
    #Create a dictionary where the keys are the numbers in the value list, and the values are the remainders of that number from the remainder list.
    #For the current key in the dictionary entered into the function, change the value to the new remainder dictionary.
    for key in dict:
        newdict={}
        for x in dict[key]:
            newdict[x]=[]
            for y in numlist:
                newdict[x].append(round(x%y,2))
        dict[key] = newdict
        print key + ": " + str(newdict)


    #Print out the new dictionary.
    print "Modified original dictionary: "
    print dict
    print 
    #Return the dictionary.
    return dict


test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]

# 1. Run the function with the default keyword argument
dictnums(test_dict)
# 2. Run the function assigning the default keyword argument to the optional list
dictnums(test_dict,optional_remainder)
