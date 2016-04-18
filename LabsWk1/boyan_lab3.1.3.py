#Author: Haley Boyan
#Review Problem 3
#function that will iterate through two lists.

def list_it(listA,listB):
    i=1
    while i<=len(listA):
        print "Iteration: %i" %i
        print "List A: " + str(listA)
        print "List B: " + str(listB)
        #Iterate through each element of both lists at the same time using a for loop,
        #assigning the number from list 1 to variable value1 and the number from list 2 to value2:
        for value1,value2 in zip(listA,listB):
            multiplied = value1*value2
            print multiplied
            #If multiplied is greater than 300, break out of the for loop and while loop.
        if multiplied>300:
            break
        #Otherwise, multiply each element of list 1 and list 2 by 2 before continuing through the while loop
        else:
            listA = [x*2 for x in listA]
            listB = [x*2 for x in listB]
        i+=1
    print "Function complete."

list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]
list_it(list1,list2)
