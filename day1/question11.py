
def check_occurrence(word:str):
    word = word.replace(" ",'')
    output = {}
    for index,char in enumerate(word):
        if char not in output:
            output[char] = 1
        else:
            output[char] += 1
            
    print(output)
        
check_occurrence('My name is kaushal gautam')