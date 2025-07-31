def convert_appearance(word):
    not_index = word.find('not')
    poor_index = word.find('poor')

    print("Index of 'not':", not_index)
    print("Index of 'poor':", poor_index)
    words = word.lower().split()
    not_index= max([ i  for i,char in enumerate(words) if char=='not'])
    print(not_index)
    
        
    
    
        

    # if not_index != -1 and poor_index != -1 and poor_index > not_index:
    #     # Replace from 'not' to end of 'poor'
    #     word = word[:not_index] + 'good' + word[poor_index + 4:]

    # print("Final output:", word)

# Input
character = input("Enter any name: ")
convert_appearance(character)
