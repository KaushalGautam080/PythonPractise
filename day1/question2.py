character = input("Enter string: ")

new_character = ''

def slice_string():
 if len(character) < 2:
     new_character = 'Empty String'
 else:
    new_character = character[:2] + character[-2:]  
    
 print(new_character)


slice_string()


