# Write a Python program to add an item in a tuple. 

fruits = ("apple","banana","pear")
print(fruits.index("pear"))
fruits_list = list(fruits)
fruits_list.append("mango")
fruits = tuple(fruits_list)
print(fruits)
