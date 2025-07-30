


def remove_odd_character(word):
    trimmed_string = ''
    for index,char in enumerate(word):
        if index % 2 == 0:
            trimmed_string += char
    
    print(trimmed_string)
    
    
remove_odd_character('hello world')