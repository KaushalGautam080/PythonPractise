# variables
# why we need variables => to store the data

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
a = b
b = temp
print("After swapping")
print(a)
print(b)
