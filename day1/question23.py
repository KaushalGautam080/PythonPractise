# Write a Python program to check a list is empty or not. 

empty_list = []

# using len
def check_empty_list():
    if len(empty_list) <=0 :
        return True
    else:
        return False


print(check_empty_list())

# using not method

def is_list_empty():
    if not empty_list:
        return True
    else:
        return False
    
print(is_list_empty())
