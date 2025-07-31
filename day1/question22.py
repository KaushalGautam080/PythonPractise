# Write a Python program to remove duplicates from a list. 

num_list = [1,24,14,124,124,35,767,899,767,13,14,24]

def remove_duplicate():
    non_duplicate_list=[]
    for i in num_list:
        if i not in non_duplicate_list:
            non_duplicate_list.append(i)
            
    print(non_duplicate_list)
    
    
remove_duplicate()