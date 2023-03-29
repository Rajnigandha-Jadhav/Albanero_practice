# 1. Abstraction :Abstraction is the concept of hiding complex details and exposing only the essential features of an object or system. In Python, abstraction is achieved using classes, which allow you to define abstract data types that can be used to create objects.

# One way to implement abstraction in Python is through the use of abstract classes and methods. 

# Abstract Class : Class having an abstract mehods.
# Abstract methods : It has only fun declaration and not the func definition.
# Concrete Class : Class w/o Abstract Methods. It inherits all the methods of an abstract class.
# Objects can't be created for abstract methods. It can be created for concrete class.

# Example 1 :=>
from abc import ABC,abstractmethod
class AbstractDemo(ABC):  #Abstract class
    @abstractmethod
    def display(self):
        None

class Demo(AbstractDemo): #Concrete class
    def display(self):
        print("concrete class")

obj = Demo()
obj.display()



# Example 2 :=>
from abc import ABC,abstractmethod
class AbstractDemo(ABC):  #Abstract class
    @abstractmethod
    def display(self):
        None

    @abstractmethod
    def show(self):
        None

class Demo(AbstractDemo): #Concrete class
    def display(self):
        print("Sould inherit all the methods")

    def show(self):
        print("Good Morning!")
obj = Demo()
obj.display()
obj.show()


# Example 3 :=>
from abc import ABC,abstractmethod
class AbstractDemo(ABC):  #Abstract class
    @abstractmethod
    def display(self):
        None

    @abstractmethod
    def show(self):
        None

class Demo1(AbstractDemo): #Abstract class
    def display(self):
        print("Sould inherit all the methods")



class Demo2(AbstractDemo): #Concrete class
    def display(self):
        print("Sould inherit all the methods to be an concrete class")

    def show(self):
        print("Have a Good Day!")
obj = Demo2()
# obj1 = Demo1() => it will create an error because now it will act as an abstarct class.
obj.display()
obj.show()


# 2. why and when to use class variables and class methods :
#          class variables create a single copy that will be used by all objects.this value is constant 
# and if we change it, it will get changed for all objects.
class Employee:
    company_name = "infosys"
    def __init__(self,n,s):
        self.name = n
        self.salary = s
    @classmethod
    def get_company_name(cls):
        cls.company_name = "Albanero"
        print(cls.company_name)

e1 = Employee('Jay',10000)
e2 = Employee('Vishal',25000)

Employee.get_company_name()
print(e2.company_name)
        
# 3. static methods
# In Python, a static method is a method that belongs to a class and does not require an instance of the class to be created before it can be called. It is defined using the @staticmethod decorator and can be called on the class itself, without instantiating any object of that class.

# A static method is similar to a class method, but the difference is that it does not take any special first argument such as the class itself or the instance of the class. It behaves like a regular function that happens to be defined inside a class.
class calculations:
    @staticmethod
    def add(a, b):
        return a + b

result = calculations.add(2, 3)
print(result) # Output: 5


class display:
    @staticmethod
    def show():
        return "Happy Birthday!"
    
a = display.show()
print(a)


class Abc:
    @staticmethod
    def bank(a,b): 
        salary = a+b
        return salary
    
x = Abc.bank(10000,50000)
print(x)