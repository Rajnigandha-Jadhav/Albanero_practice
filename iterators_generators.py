# A process that is repeated more than one time by applying the same logic is called an Iteration. 
# If the loop is executed 6 times continuously, then we could say the particular block has iterated 6 times. 

a = [0, 5, 10, 15, 20]
for i in a:
    if i % 2 == 0:
        print(str(i)+' is an Even Number')
    else:
        print(str(i)+' is an Odd Number')

# OUTPUT =>
# 0 is an Even Number
# 5 is an Odd Number
# 10 is an Even Number
# 15 is an Odd Number
# 20 is an Even Number


# An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc.
# Using an iterator-

# iter() keyword is used to create an iterator containing an iterable object.
# next() keyword is used to call the next element in the iterable object.
# After the iterable object is completed, to use them again reassign them to the same object.

iter_list = iter(['Geeks', 'For', 'Geeks'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))



list1 = [2, 4, 8, 9]
itr = iter(list1)
try:
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    
except StopIteration:
    print("No more elements to iterate over.")




# Create a list
my_tuple = (1, 2, 3, 4, 5)

# Create an iterator object
my_iter = iter(my_tuple)

# Loop through the iterator using a try-except block
try:
    while True:
        # Get the next item from the iterator
        item = next(my_iter)
        print(item)
except StopIteration:
    print("End of iterator reached.")




dict1 = {"name": "Pari", "age": 2, "school": "NPS"}
itr1 = iter(dict1.items())

try:
    while True:
        ele = next(itr1)
        print(ele)
except StopIteration:
    print("End of iterator")





# Generators : It is another way of creating iterators in a simple way where it uses the keyword “yield” instead of returning it in a defined function.
def sq_numbers(n):
	for i in range(1, n+1):
		yield i*i


a = sq_numbers(3)

print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))
