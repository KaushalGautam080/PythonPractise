def check(func):
    def wrapper():
        print("Before calling the function")
        
        func()
        print("After calling the function")
        
    return wrapper


def greet():
    
    print("Hello")
    
@check
def sing():
    print("Iam singing")
    
sing()