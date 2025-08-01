character = input('Enter any string: ')

new_character = ''

def replace_string():
    global new_character 
    first_char = character[0]
    
    for index, char in enumerate(character):
        if index == 0:
            new_character += char  
        elif char == first_char:
            new_character += '$'
        else:
            new_character += char
    print(new_character)

replace_string()
