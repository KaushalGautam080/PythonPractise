character = input("Enter any name: ")



def appendString(word):
    if len(word) <3:
        word
        
    elif  word.endswith('ing'):
        word += 'ly'
    else:
        word += 'ing'
        
    print(word)
    
appendString(character)