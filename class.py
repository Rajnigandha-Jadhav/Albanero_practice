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
# class Firstclass:
#     def show(self):
#          print("hi,how are u?")
# x = Firstclass()
# x.show()


# # 2) Example2:
# class Mobile:
#      def __init__(self):
#           self.model = "Vivo Y12G"
#      def display_model(self):
#           print("Model:", self.model)

# a = Mobile()

# a.display_model()
# print(a.model)

# a.model = "Galaxy J2"
# print(a.model)



# # 3) Example3:
# class Fridge:
#      def __init__(self,m):
#           self.type = m
#      def display(self,n):
#           brand = n
#           print("Type:",self.type, "Brand:",brand)

# f = Fridge("Double Door")
# f.display("Whirpool")
# print(id(f))

# fr = Fridge("Single Door")
# f.display("Samsung")
# print(id(fr))


# Constructor :
class Mobile:
     def __init__(self,m,lr):
          self.model = m
          self.launch_year = lr
     def highlight(self,p):
          price = p
          print("model name:",self.model, "launched in the year:",self.launch_year, "at the price:",price)

obj = Mobile("Redmi",2023)
obj.highlight(15000)
print(obj.model)



class Albanero:
     def __init__(self):  #constructor
          self.designation = "Product Lead"  #instance variable
     def company(self):   #instance method
          print(self.designation)

organization = Albanero()
print(organization.designation)


# CLASS Variable :=>
class Bank:
     cv = "Fix Deposit"
     @classmethod
     def account(cls):
          print(cls.cv)

object = Bank()
print(object.cv)
object.account()


class Job:
     a = "Good Job"
     def __init__(self):
          self.opportunity = "Hardwork"
     def success(self):
         print("Success:",self.opportunity)
     @classmethod
     def access(cls):
          print("Future:",cls.a)

albanero = Job()
albanero.success()
albanero.access()

class Abc:
     def __init__(self):
          self.pqr = "hi"
     def xyz(self):
          return f"it should print {self.pqr}"
     
obj = Abc()
print(obj.xyz())