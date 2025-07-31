sample_list =  ['apple', 'banana', 'grape', 'kiwi', 'avocado']



def sort():
    result = 0
    for i in sample_list:
        first_char = i[:1]
        last_char = i[-1:]
        if len(i) >=2 and first_char == last_char:
            result += 1
            
    print(result)
        
        
sort()