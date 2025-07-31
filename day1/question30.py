
#  Write a Python script to check whether a given key already exists in a dictionary
sample_dict =  {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
new_key = 9

def check_duplicate_key():
        return new_key in sample_dict
            
if(check_duplicate_key()):
    print("Key already exists")
else:
    print("Key donot exist")
    
