#
# PSP Assignment 2 Module 201502
#
# File:      list_function.py
# Author:    Daniel Arbon
# SAIBT Id:  arbdtd1502
# Description:  This is the file of created list functions.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

#
# Write your function definitions in this file.
#


# Function length()
def length(my_list):
    listLength = 0 # Create list length counter with default value of '0'.
    for item in my_list: # Increment the counter by 1 for each item in the list.
        listLength += 1
    return listLength # Return the list length counter.


# Function to_string()
def to_string(my_list,sep = ', '):    
    outString = "List is: " # Create a variable to store the string result.
    if length(my_list) > 0: # If the list has items in it,
        for index in range(0,(length(my_list)-1)):
            outString += str(my_list[index]) + sep # convert each item (except the last)to a string and add the separator.
        outString += str(my_list[-1]) # Then add the last item to the end of the string.
    return outString # Return the string.


# Function count()
def count(my_list, value):  
    itemCount = 0 # Create a counter variable.
    for item in my_list: # Check if each item in the list matches the 'value' parameter.
        if item == value:
            itemCount += 1 # IF yes: increment the counter variable.
    return itemCount # Return the count.


# Function find()
def find(my_list, value):    
    matchIndex = -1 # Create an variable to store an index, with default value "-1".
    for index in range(0, length(my_list)): # Search through the list...
        if my_list[index] == value: # ... if an item in the list matches the value parameter,
            matchIndex = index # Store the index of the matching item.
    return matchIndex # return the index of the matching item, or -1 if no match.


# Function starts_with()
def starts_with(list1, list2):  
    if length(list2) < length (list1): # First, check if list2 can fit inside list1.
        matches = 0 # Store a count of matching values.
        for index in range(0, length(list2)):
            if list1[index] == list2[index]: # Check if the values of list2 and list1 match.
                matches += 1 # IF yes: increment the match counter.
            else:
                matches += 0
        if matches == length(list2): # If the all of list2 is matched, "starts with" is True.
            return True
        else:
             return False # If it does not all match, list2 is not in list1.
    else:
        return False # If list2 is longer than list1, it is not inside list1.
    

# Function remove_value()
def remove_value(my_list, value): 
    shortList = [] # Store the shortened list.
    for item in my_list:
        if item != value:
            shortList.append(item) # Add items to the new list UNLESS they match the value to be exluded.
    return shortList # return the shortened list.

# Function insert()
def insert(list1, list2, index):
    listPos = 0
    longList = []
    if index > length(list1): # If index is greater than list1 is long, add list2 to the end.
        longList = list1
        for item in list2:
            longList.append(item)
    elif index < 0: # If the index is less than 0...
        for item in list2: # ...add list2 first...
            longList.append(item)
        for item in list1: # ...and then list1.
            longList.append(item)
    else: # If index is inside range of list1.
        while listPos < index:
            longList += list1[listPos] # Add the first part of list1 to the new list.
            listPos += 1
        for item in list2: # Then add list2.
            longList.append(item)
        for num in range(index,length(list1)): # Then add the rest of list1.
            longList.append(list1[num])
    return longList

# Function reverse()
def reverse(my_list):
    backList = [] # Store the reversed copy of my_list.
    if length(my_list) > 0:
        for num in range(length(my_list)-1,0,-1): # Iterate through my_list in reverse order.
            backList.append(my_list[num]) # Append each item to the new list.
        backList.append(my_list[0]) # Add the last item to the new list.
    return backList
        

