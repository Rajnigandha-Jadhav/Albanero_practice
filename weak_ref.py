# In Python, garbage collection is the process of automatically freeing up memory that is no longer being used by an application. When an object in memory is no longer being referenced by any part of the program, it becomes eligible for garbage collection, and its memory is freed up.

# Python's garbage collector works by using a reference counting mechanism. Each object in memory has a reference count that indicates how many references point to it. When an object's reference count reaches zero, it is no longer being used and can be safely removed from memory.

# However, there are cases where objects can reference each other in a way that creates a cycle of references, meaning that no object in the cycle has a reference count of zero. To deal with these cases, Python provides weak references.

# A weak reference is a reference to an object that does not increase its reference count. This means that if an object has only weak references pointing to it, it is still eligible for garbage collection even if the weak references are still alive.




import weakref

class MyClass:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("info :",self.name)

a = MyClass("object a")

b = MyClass("object b")
a.show()
print(a.name)
a_ref = weakref.ref(a)
b_ref = weakref.ref(b)

print(a_ref()) 
print(b_ref())  

del a  # delete the strong reference to object a
print(a_ref())  # prints: None

# In this example, we create two instances of a class MyClass and store them in variables a and b. We then create weak references a_ref and b_ref to a and b respectively.

# When we delete the strong reference to a by using the del statement, the reference count for a becomes zero, but b still has a reference to a, so a is not eligible for garbage collection yet. However, since the weak reference a_ref does not increase the reference count of a, a is still eligible for garbage collection even though b still has a reference to it.

# When we try to access a_ref after deleting the strong reference to a, we get None instead of an object, indicating that a has been garbage collected.

# In summary, garbage collection is the process of automatically freeing up memory that is no longer being used by an application, and weak references are references to objects that do not increase their reference count, making them eligible for garbage collection even if they are still being referenced by other objects.


import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
weakref_obj = weakref.ref(obj)
print(weakref_obj())  # Output: <__main__.MyClass object at 0x7fb867a3ed10>
del obj  # Delete the original object

if weakref_obj() is None:
    print("The original object has been garbage collected")
else:
    print("The original object still exists")



class MyClass:
    x = "albanero"
    def __init__(self, name):
        self.name = name
    def show(self):
        print("info :",self.name)

t1 = MyClass()
t2 = t1
t3 = t2

t1 = None
t2 = None