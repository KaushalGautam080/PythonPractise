# 32. Write a Python script to generate and print a dictionary that contains a 
# number (between 1 and n) in the form (x, x*x). 



num = 5  
result ={}  
def generate_dict(number):
    while not number <= 0:
        result.update({number:pow(number,number)})
        number -= 1
        
    print(result)
    
generate_dict(num)
        
        