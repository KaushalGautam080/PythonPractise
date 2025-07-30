# character = input('Enter any name')
# index = int(input('Enter any number'))

def remove_character(word: str,index:int):
    if len(word)< index or len(word) <=0:
        print('Insufficient index for the given word')
        return()
        
    print(word[:index]+word[index + 1:])
        
        
    
    
remove_character('abcdef',4)
    
        