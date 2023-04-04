# class Test:
#     def __init__(self):
#         print("1-arg constructor")
#     def __init__(self):
#         print("2-arg constructor")

# t1 = Test()



class InvalidAge(Exception):
    pass
try:
    n = int(input("enter the age:"))
    if n<=0:
        raise InvalidAge("Age can not be less than or equal to zero")
    print("Age of a person:",n)
except InvalidAge as var:
    print(var)
print("End of the program...")


class FiveDivisionError(Exception):
    pass
try:
    n1 = int(input("Enter a first number:"))
    n2 = int(input("Enter a second number:"))
    if n2 == 5:
        raise FiveDivisionError("Can't devide by 5")
    div = n1/n2

except (FiveDivisionError,ZeroDivisionError) as var:
    print(var)
print("Program Execution completed...")
