#
#  PSP Assignment 2, Part I - Test File  201502
#
#  DO NOT MODIFY THIS FILE!
#

import list_function

str_list1 = ['r','i','n','g','i','n','g']
str_list2 = ['b', 'o', 'o', 'm']
str_list3 = ['r', 'e', 'd']
str_list4 = ['r', 'i']
empty = []

print("Start Testing!")
print("\nlength Test")
print("List length:", list_function.length(str_list1))
print("List length:", list_function.length(empty))

print("\nto_string Test")
print(list_function.to_string(str_list1))
print(list_function.to_string(str_list1, "-"))
print(list_function.to_string(empty))      

print("\ncount Test")
print(list_function.count(str_list1,'n'))
print(list_function.count(str_list1,'a'))
print(list_function.count(empty,'n'))

print("\nfind Test")
print(list_function.find(str_list1, 'g'))
print(list_function.find(str_list1, 'a'))

print("\nstarts_with Test")
print(list_function.starts_with(str_list1, str_list4))
print(list_function.starts_with(str_list4,str_list1))
print(list_function.starts_with(str_list1,str_list2))#***********************


print("\nremove_value Test") 
print(list_function.remove_value(str_list1, 'n'))
print(list_function.remove_value(str_list1, 'r'))

print("\ninsert Test")
print(list_function.insert(str_list2, str_list3,2))
print(list_function.insert(str_list3, str_list2,10))
print(list_function.insert(str_list2, str_list3,10))


print("\nreverse Test")
print(list_function.reverse(str_list1))
print(list_function.reverse(empty))


print("\n----------")


num_list = [1, 7, 2, 3, 7, 7]
short_list = [1]
other_list = [1, 2, 3, 4, 5, 6]
seven_list = [7]

print("\nlength Test")
print("List length:", list_function.length(num_list))

print("\nto_string Test")
print(list_function.to_string(num_list))
print(list_function.to_string(num_list, " - ")) 

print("\ncount Test")
print(list_function.count(num_list, 4))

print("\nfind Test")
print(list_function.find(num_list, 4))

print("\nstarts_with Test")
print(list_function.starts_with(num_list, short_list))
print(list_function.starts_with(num_list,other_list))

print("\nremove_value Test") 
print(list_function.remove_value(num_list, 7))

print("\ninsert Test")
print(list_function.insert(other_list, seven_list,10))   

print("\nreverse Test")
print(list_function.reverse(num_list))

print("\nEnd Testing!\n")


