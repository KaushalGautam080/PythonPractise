character = input('Enter any string: ').split(',')

char1 = character[0]
char2 = character[1]
print(char1)
print(char2)

print(f"{char2[0:3] + char1[3:]}  {char1[:3] + char2[3:] }")
