
# Write a Python script to print a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are square of keys 

sample_dict = {
  1: 1,
  2: 4,
  3: 10,     # intentionally not 9
  4: 16,
  5: 26,     # intentionally not 25
  6: 36,
  7: 50,     # intentionally not 49
  8: 64,
  9: 81,
  10: 100,
  11: 122,   # intentionally not 121
  12: 144,
  13: 169,
  14: 195,   # intentionally not 196
  15: 225
}


def filter_dict():
    new_dict={}
    for x,y in sample_dict.items():
        if x >= 1 and x <= 15 and x*x == y:
            new_dict.update({x:y})
            
    return new_dict

print(filter_dict())


