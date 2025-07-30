character = input("Enter any name: ")



def appendString(word):
    if  word.endswith('ing'):
        word += 'ly'
    else:
        word += 'ing'
        
    print(word)
    
appendString(character)