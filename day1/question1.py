

def countCharacter():
    character = input("Enter any string: ")
    string_dict = {}
    print(character)
    for i in character:
        if i not in string_dict:
            string_dict[i] = 1
        else:
            string_dict[i] += 1
    print(string_dict)
        
    
    
    

countCharacter()