# try
# except
# else
# finally


# try => block in which those lines if codes are placed which might contain error
# except => block in which statements related to handle exception are written
# else => block in which executes after try block execute successfully(no exception found in try block)
# finally => whether try or except it gets executed

a = int(input("Enter first number"))
b = int(input("Enter second number"))

try:
    c = a/b
    print("output:", c)
except ZeroDivisionError:
    print('Cannot divide by zero!')
except Exception as e:
    print(f"Oops error occurred and is caused by {e}")
else:
    print("program executed successfully")
finally:
    print("It is always executed")


