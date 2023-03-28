# Inheritance : In Python, inheritance allows a subclass (also called derived class) to inherit methods and properties 
# from a superclass (also called base class).

# Single Inheritance :
class Superclass:
    def inheritance(self):
        print("hello")


class Subclass(Superclass):
    print("hi")

obj = Subclass()
obj.inheritance()




class Father:
    money = 1000

    def show(self):
        print("child class")

    @classmethod
    def showmoney(cls):
        print("parent class method:",cls.money)

class Son(Father):
    def display(self):
        print("child class method")

s = Son()
s.display()
print(s.money)
s.show()


# Multiple Inheritance :
# In Python, multiple inheritance is a feature that 
# allows a class to inherit from multiple parent classes. 


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class DogCat(Dog, Cat):
    pass

dc = DogCat("Fido")
print(dc.speak()) # Output: Woof!
