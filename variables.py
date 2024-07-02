# variables
# why we need variables => to store the data


# Variables naming rules.
# - It should be meaningful
# - Only alphanumeric is required
# - Variable name should start with underscore or alphabetic letter

# Program to swap two numbers
name = input("What is your name? ")
print(name)
length = len(name)
print(f"Your name has {length} characters")

# Program to swap two number
a = input("Enter value of a")
b = input("Enter value of b")

print("Before swapping")
print(a)
print(b)
temp = a

b = temp
print("After swapping")
print(a)
print(b)
