#Errors in python : Errors are the problems or the faults that occur in the program, 
#                   which makes the behavior of the program abnormal.

# Exceptions in python :  An exception is an event, which occurs during the execution of a program, 
#                         that disrupts the normal flow of the program's instructions.(runtime error)

# Types of Exceptions:
# 1)ZeroDivisionError:
    #   ex. print(10/0)


# 2)Type Error:
#       print("10"+10)

# 3)Value Error:
#       print(int("hi"))

# 4)Index Error:
#       list1 = [1,2,3]
#       print(list1[4])

# 5)Key Error:
#       dict1 : {"name":"abc","age":10}
#       print(dict1["height"])

# 6)ModuleNotFoundError:
#       importing a module that is not present.

# 7)Import Error:
#      importing the module with correct module name but function name written incorrectly.




# Errors in python :=>
#1) Syntax Error:
#    ex. print( "hello"


#2) Name Error:
# print(x)

#3) Indentation Error:
# for i in range(10)
# print(i)


# Exception Handling :=>
# try:
#     x = 1/0
#     print(x)
# except:
#     print("can't devide by zero")
# finally:
#     print("The program has finished")


# try:
#     a = int("hello")
#     print(a)
# except ValueError:
#     print("invalid integer")
# except:
#     print("An exception occured")


# try:
#     a = 10/5
# except:
#     print("error")
# print(a)