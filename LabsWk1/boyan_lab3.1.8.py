#Author: Haley Boyan

#Dictionaries:
first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

#Accept one argument which will be a dictionary.
def string_intlist_cleaner(dict):
    #Iterate through the key:value pairs in the dictionary:
    temp_dict = {}
    for item in dict:
        #If the key is not a string, remove the key:value pair from the dictionary.
        #If the value is not a list, remove the key:value pair from the dictionary.
        if type(item) is str and type(dict[item]) is list:
            temp_dict[item] = dict[item]
    #Return the "cleaned" dictionary.
    dict = temp_dict
    return dict

#Accept one argument which will be a dictionary.
def int_string_cleaner(dict):
    temp_dict = {}
    #Iterate through the key:value pairs in the dictionary:
    for item in dict:
        #If the key is not an integer, remove the key:value pair from the dictionary.
        #If the value is not a string, remove the key:value pair from the dictionary.
        if type(item) is int and type(dict[item]) is str:
                temp_dict[item] = dict[item]
    #Return the "cleaned" dictionary.
    dict = temp_dict
    return dict

#Accept two arguments which will be dictionaries.
def dict_cleaner(dictA,dictB):
    #Print the first dictionary.
    print("Dictionary 1: ")
    print dictA
    print
    #Print the second dictionary.
    print("Dictionary 2: ")
    print dictB
    print

    #Assign the cleaned version of the first dictionary to a variable, calling your function
    #string_intlist_cleaner() with the first dictionary as an argument.
    cleanA = string_intlist_cleaner(dictA)
    #Assign the cleaned version of the second dictionary to a variable, calling your function
    #int_string_cleaner() with the second dictionary as an argument.
    cleanB = int_string_cleaner(dictB)

    #Combine the two cleaned dictionaries.
    totalclean={}
    for item in cleanA:
        totalclean[item] = cleanA[item]
    for item in cleanB:
        totalclean[item] = cleanB[item]

    #Print the combined and cleaned dictionary.
    print("All cleaned up: ")
    print totalclean
    print
    #Return the combined and cleaned dictionary.
    return totalclean

dict_cleaner(first_dict,second_dict)
