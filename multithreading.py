# Multithreading is a technique in which multiple threads of execution run concurrently within a single process. Python provides a built-in module threading for multithreading.
import threading

def worker():
   
    print('Worker thread is running...')

# Create a new thread
thread = threading.Thread(target=worker)
# Start the thread
thread.start()



import threading

def thread_job():
    print("This is an example of a thread job.")


t = threading.Thread(target=thread_job)
t.start()




import threading

def thread_job(x, y):
    print(f"The sum of {x} and {y} is {x+y}.")


t = threading.Thread(target=thread_job, args=(2, 3))
t.start()



import threading

class MyThread(threading.Thread):
    def __init__(self, x, y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y

    def run(self):
        print(f"The sum of {self.x} and {self.y} is {self.x+self.y}.")


t = MyThread(5,6)
t.start()
