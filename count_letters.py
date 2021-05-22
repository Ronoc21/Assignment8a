# Name: Conor Smith
# Date: 5/19/21
# Description: Takes a string and counts how many letters and returns a dictionary that gives a count of each number
# the key is the letter the paired value is the number of times the key occurred

def count_letters(string):
    """creates a dictionary that counts the number of times letter occur."""
    dictionary = {}
    for i in string.upper():
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

#print(count_letters("aksdaslKLAJSdlkf265456JASdaljsdfla"))