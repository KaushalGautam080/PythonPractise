from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'
    PINK = 'pink'


color = Color(input("Enter the color of your choice"))

match color:
    case Color.RED:
        print("red color")
    case Color.GREEN:
        print("green color")
    case Color.YELLOW:
        print("yellow color")
    case _:
        print("Cant find the correct color")

