# Package : A collection of modules.

# Importing * From a Package :=>  

# a package called my_package that contains three modules: module1.py, module2.py, and module3.py. 
# If you use the syntax 
# from my_package import * 
# Python will import all three modules into your current namespace.


# Intra-package References :=>
# a package called mypackage, which contains two modules, module1 and module2. 
# If you want to refer to a function called myfunction in module1 from module2, 
# you can use an intra-package reference like this:=>

# from mypackage.module1 import myfunction



# Formatted String Literals :=> In Python, formatted string literals, also known as f-strings, 
# are a way to embed expressions inside string literals.

name = "abc"
school = "JNV"
print(f"my name is {name} and I am from {school} school.")

a = 10
b = 20
print(f"The product of {a} and {b} is {a*b}")