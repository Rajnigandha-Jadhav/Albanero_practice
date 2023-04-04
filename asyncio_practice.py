# asyncio is a Python library that provides a way to write asynchronous code using coroutines. It was introduced in Python 3.4 and provides a way to write concurrent code in a single-threaded, cooperative multitasking environment.

# The asyncio library uses an event loop to manage the execution of coroutines. Coroutines are functions that can be paused and resumed, allowing other coroutines to run in the meantime. The event loop is responsible for scheduling the execution of coroutines and switching between them when they are paused or resumed.

# asyncio provides a number of tools for working with coroutines, including:

# async and await keywords for defining and working with coroutines.
# Future objects for representing the result of an asynchronous operation.
# Task objects for running coroutines concurrently and managing their state.
# asyncio.sleep for suspending the execution of a coroutine for a given period of time.
# asyncio.wait and asyncio.gather for waiting for multiple coroutines to complete.
# Overall, asyncio provides a powerful and flexible way to write asynchronous code in Python, making it easier to write efficient and responsive applications.


import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(2)
    print("Coroutine finished")

async def main():
    print("Main started")
    await asyncio.gather(my_coroutine(), my_coroutine())
    print("Main finished")

asyncio.run(main())



import asyncio

async def my_coroutine():
    print("started")
    await asyncio.sleep(2)
    print("finished")

asyncio.run(my_coroutine())




import asyncio

async def my_coroutine():
    print("starting")
    await asyncio.sleep(2)
    print("finished")

async def main():
    task = asyncio.create_task(my_coroutine())
    print("Main started")
    await task
    print("Main finished")

asyncio.run(main())
