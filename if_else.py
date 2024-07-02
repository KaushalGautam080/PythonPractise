# num = int(input("Please enter any number: "))
# if num < 0:
#     num = 0
#     print("Input value changed to 0")
# elif num == 0:
#     print("You entered 0")
#
# else:
#     print("None ")

age = int(input("Enter your age "))

if age < 18:
    print("You are not eligible")
elif age > 24 & age < 65 :
    print("You are perfect to go")
else:
    print("You're over aged ")

traffic_light = "green"
if traffic_light == "red":
    print("stop")
elif traffic_light == "green":
    print("go")
elif traffic_light == "yellow":
    print("look")
