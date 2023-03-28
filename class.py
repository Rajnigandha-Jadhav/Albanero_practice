# CLASS :=> A python class is a group of attributes and methods.

# ATTRIBUTES :=> Attributes are represented by variable that contains data.

# METHOD :=> Method performs an action or task. It is similar to function.

# HOW TO CREATE A CLASS :=>
# class Classname(object):
#     def __init__(self):
#         self.variable_name = value
#         self.variable_name = "value"
#     def method_name(self):
        # Body of Method


# Class keyword is used to create a class.
# object represents the base class name from where all classes in python are derived.
# __init__() method is used to initilise variables.It is called constructor.
# self is a variable which refers to the current class or instance.


# 1) Example1:
class Firstclass:
    def show(self):
         print("hi,how are u?")
x = Firstclass()
x.show()


# 2) Example2:
class Mobile:
     def __init__(self):
          self.model = "Vivo Y12G"
     def display_model(self):
          print("Model:", self.model)

a = Mobile()

a.display_model()
print(a.model)

a.model = "Galaxy J2"
print(a.model)



# 3) Example3:
class Fridge:
     def __init__(self,m):
          self.type = m
     def display(self,n):
          brand = n
          print("Type:",self.type, "Brand:",brand)

f = Fridge("Double Door")
f.display("Whirpool")
print(id(f))

fr = Fridge("Single Door")
f.display("Samsung")
print(id(fr))