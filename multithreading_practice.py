# Multithreading is a technique in which multiple threads of execution run concurrently within a single process. Python provides a built-in module threading for multithreading.
# import threading

# def worker():
   
#     print('Worker thread is running...')

# # Create a new thread
# thread = threading.Thread(target=worker)
# # Start the thread
# thread.start()



# import threading

# def thread_job():
#     print("This is an example of a thread job.")


# t = threading.Thread(target=thread_job)
# t.start()




# import threading

# def thread_job(x, y):
#     print(f"The sum of {x} and {y} is {x+y}.")


# t = threading.Thread(target=thread_job, args=(2, 3))
# t.start()



# import Thread class...
from threading import Thread,current_thread
# create a function containing code to be executed parallaly.
def display(n,msg):  # executed by t1 thread
    print("t1 thread details:",current_thread().ident)
    for i in range(n):
        print(msg)

t1 = Thread(target=display,kwargs={"n":4,"msg":"hi"})
t1.start()

print("main thread:",current_thread().name)
for i in range(5):  #executed by main thread.
    print("welcome")



# Creating threads for methods
from threading import Thread

class Example:
    def display(self,n):
        for i in range(n):
            print("Hello")

e1 = Example()
t2 = Thread(target=e1.display,args=(2,))
t2.start()
            
for i in range(4):
    print("Welcome")


# creating thread for class methods
class Practice:
    @classmethod
    def show(self,n):
        for i in range(n):
            print("good morning")


t3 = Thread(target=Practice.show,args=(4,))
t3.start()

for i in range(4):
    print("bye")


# creating thread for static methods
class City:
    @staticmethod
    def village(m):
        for i in range(m):
            print("Thanks")


t4 = Thread(target=City.village,args=(6,))
t4.start()

for i in range(2):
    print("hmmmm")


# Creating threads by extending thread class :
from threading import Thread
videos = ["OOP","Class","packages"]
class Myclass(Thread):
    def __init__(self,val):
        self.kid = val
        Thread.__init__(self)

    def show(self):
        print("Learning Python")

    def run(self):
        self.show()

        if self.kid:
            print("kids can watch")

        for i in videos:
            print(i)

v1 = Myclass(True)
v1.start()

for i in range(4):
    print("informative videos")


# thread names and ids
from threading import Thread,current_thread
import os
def show():
    print("hi")

def display():
    print("hello")

t1 = Thread(target=show)
t2 = Thread(target=display)
t1.start()
t2.start()
t1.name = "Abdul"
t2.name = "Mahesh"
print(t1.name)
print(t2.name)
print(current_thread().ident)
current_thread().name = "Jay"
print(current_thread().name)
print(t1.ident)
print(os.getpid())



