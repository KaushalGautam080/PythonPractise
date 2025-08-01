# Write a Python program to clone or copy a list. 


num_list = [1,2,3,4,5,6,6,6,6,768]

# using in-built copy method
new_list = num_list.copy()
print(new_list)
 
# using list comprehension
comp_list = [i for i in num_list]
print(comp_list)

# using list method 
# if list not assigned then also copied 
copy_list = list(num_list)
print(copy_list)