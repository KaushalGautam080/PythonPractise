def longest_word(sentence:list):
    length = 0
    for i in sentence:
        if length < len(i):
            length = len(i)
    print(length)
    return length

fruits = ["apple", "banana", "cherry"]
longest_word(fruits)