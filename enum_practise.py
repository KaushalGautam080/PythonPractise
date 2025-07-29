# from enum import Enum


# # class Color(Enum):
# #     RED = 'red'
# #     GREEN = 'green'
# #     YELLOW = 'yellow'
# #     PINK = 'pink'


# # color = Color(input("Enter the color of your choice"))

# # match color:
# #     case Color.RED:
# #         print("red color")
# #     case Color.GREEN:
# #         print("green color")
# #     case Color.YELLOW:
# #         print("yellow color")
# #     case _:
# #         print("Cant find the correct color")

# class Constansts(Enum):
#     width = 100
#     height = 150

# print(Constansts.width.value)



# name = input('What is your name')
# print(name)

condition = True
name = "Roger"

if condition == True:
    print("The condition")
    print("was True")
elif name == "Roger":
    print("Hello Roger")
elif name == "Syd":
    print("Hello Syd")
elif name == "Flavio":
    print("Hello Flavio")
else:
    print("The condition")
    print("was False")