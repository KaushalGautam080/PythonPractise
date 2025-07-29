

 



# class Animal:
#     def walk(self):
#         print("Animal is walking")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
        
        
# jimy = Dog()
# jimy.walk()
# jimy.bark()


class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
    def desc(self):
        print(f"Animal is {self.name} and its color is{self.color}")
        
dog = Animal("dog","red")
dog.desc()
 
dog = Animal("Cow","white and black")
dog.desc()

class Dog(Animal):
    pass
    
dog1 = Dog("jimmy","yellow")
dog1.desc()