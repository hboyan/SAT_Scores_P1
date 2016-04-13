#Author: Haley Boyan

#Dictionary data:
input_dict = {
    'list':[1,2,3,4],
    'tuple':('cat', 'dog'),
    'integer':1,
    'float':99.99,
    1:'integer',
    2:'integer_2',
    'Uppercase_string':'ABCD',
    'CHARACTER':'C'
    }

#Accept 1 argument, which is a dictionary.
def dict_changes(dict):
    #Print the dictionary.
    print("Step 1: Print Dictionary: ")
    print(dict)
    print

    #Iterate through the key:value pairs of the dictionary.
    temp_dict={}
    for item in dict:
        x = str(item)
        x = x[0]
        #For pairs where the key starts with a lowercase vowel, change the value to "vowel".
        if x in "aeiou":
            temp_dict[item] = "vowel"
        #For pairs where the key starts with a lowercase consonant, change the value to "consonant".
        elif x in "bcdfghjklmnpqrstvwxyz":
            temp_dict[item] = "consonant"
    dict = temp_dict

    #Print the modified dictionary.
    print "Step 2: Make Changes: "
    print(dict)
    #Return the modified dictionary.
    return(dict)

dict_changes(input_dict)
