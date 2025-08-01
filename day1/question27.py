#  Write a Python program to replace the last element in a list with another list. 

list1= [1, 3, 5, 7, 9, 10]
list2= [2, 4, 6, 8]

def replace_last_element():
    new_list = list1[:-1] + list2
    return new_list


print(replace_last_element())
    
