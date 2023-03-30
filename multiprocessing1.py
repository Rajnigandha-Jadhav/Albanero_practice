# What is multiprocessing?

# Multiprocessing refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently.


# Why multiprocessing?

# Consider a computer system with a single processor. If it is assigned several processes at the same time, it will have to interrupt each task and switch briefly to another, to keep all of the processes going.
# This situation is just like a chef working in a kitchen alone. He has to do several tasks like baking, stirring, kneading dough, etc.

# from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))



import multiprocessing as mp
import time
import math

a = []
b = []
c = []

def calculations1(numbers):
    for n in numbers:
        a.append(math.sqrt(n))


def calculations2(numbers):
    for n in numbers:
        b.append(math.sqrt(n**2))


def calculations3(numbers):
    for n in numbers:
        c.append(math.sqrt(n**4))

if __name__ == '__main__':
    numbers_list = list(range(5))

    p1 = mp.Process(target=calculations1,args=(numbers_list,))
    p2 = mp.Process(target=calculations2,args=(numbers_list,))
    p3 = mp.Process(target=calculations3,args=(numbers_list,))

    start1 = time.time()
    p1.start()
    p2.start()
    p3.start()
    end1 = time.time()
    print(end1-start1)


    temp_a = a
    temp_b = b
    temp_c = c
    start = time.time()
    calculations1(numbers_list)
    calculations2(numbers_list)
    calculations3(numbers_list)
    end = time.time()
    print(end-start)

    print(temp_a == a)
    print(temp_b == b)
    print(temp_c == c)



