class Car:
    manufacture_year = "1992"

    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def welcome(self):
        print("Welcome Student", self.firstname)


class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def average(self):
        print(f"The average marks of {self.name} is {(self.sub1 + self.sub2 + self.sub3) / 3}")


s1 = Student("Ram", 99, 98, 97)
s1.average()
