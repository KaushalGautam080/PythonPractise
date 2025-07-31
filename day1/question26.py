# Write a Python program to insert a given string at the beginning of all items in 
#  a list. 


sample_list = [1,2,3,4]

def append_string():
    for i,c in enumerate(sample_list):
        sample_list[i] = 'emp' + str(c)
    return sample_list
        

def insert_string():
    return ['emp' + str(c) for c in sample_list]
    

print(insert_string())