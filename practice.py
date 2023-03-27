#print() == console.log()
# for(let i=1; i<11; i++){
#     console.log(i)
# }

# for i in range(1,11):
#     print(i)
# print("hello")


# function prime(N){
#     let flag = true
#     for(let i=2; i<N; i++){
#     if(N%i == 0){
#     flag = false
#     }
#     }
#     if(flag){
#        return true
#     }else{
#     return False
#     }
# }
#console.log(prime(23))


# def prime(N):
#     flag = True
#     for i in range(2,N):
#         if(N%i == 0):
#             flag = False
#     if(flag):
#         return "Yes"      
#     else:
#         return "No"
# print(prime(33))   
# 


# a = b = c = 10
# print(b)

# x,y,z = 11,12,14
# w = "hi"
# print(y)
# print(type(z))
# print(type(w))


# m,n = 11, "practice"
# print(type(n))

# c,d = 11,True
# print(c+d)

# t,y = "hi","hello"
# print(t+y)


# TOKENS :=> In python every logical line of code is broken down into components known as tokens...
# hi = "ty"
# print(type(hi))

# Keywords :=> Keywords are the set of words that can't be used to declare variables...
# Identifiers :=> Identifier is the name used to identify a variable, function, class or object...
 # Rules :=> Keywords and special charachters (except _) can't be used as indentifiers, 
      #only underscore and alphabets can be used as a starting of the identifiers, you can use digits but not at the start of an identifier...
      #As python is case sensitive, 'Var' and 'var' are 2 different identifiers...

# Example :=>
# ab12 = "hi"
# print(ab12)

# _123 = 16
# print(_123)

# x = 20
# print(x)

# _cd = "hello"
# print(_cd)


# Data Structures in Python :=> Structure used to organise, store and maintain data.
# A) => Built In Data Structure
#    1. List => It is like an array in javascript.
#list = [1, 2, 3, "hi", 5]
#       We can perform diff opn on list by using diff funcs
#       i) To add data in a list :=>
#          => append() : It adds data at the end of a list in groups if u want to add more than one.
                       #list.append((10,11))
                       #print(list)
#          => extend() : It adds data at the end of the list seperately unlike append() 

#                        list.extend((6,))                  
#                        print(list)

#          => insert() : It adds data at particular index
#                       list.insert(3,"hello")
#                       print(list)

#     ii) To delete data in a list :=>
#         => del : del keyword delets an ele of the index given.
                  # del list[2]  => will delete 3 from the list
                  # print(list)

#         => pop() : it also deletes an ele of the index given...
#                    a = list.pop(4)
#                    print(a)

#         => remove() : it removes the ele given by us in the function.
#                       list.remove("hi")
#                       print(list)

# Sort list in ascending and descending order =>
# list = [1,4,11,2,7,3,16]
# print(sorted(list))


# list.sort(reverse=True)
# print(list)

# print(list.index(16)) : It prints the index of the given no inside the index function.
# print(list.count(4)) : It counts the occurance of the given no.

#    2. Dictionary : It holds key value pairs enclosed inside a curly bracket.
# dict = {1:"hi", 2:123}
# print(dict)

# Change values inside dictionary..
# dict[2] = "python"  //write the key to change its value.
# print(dict)


# Add values inside dictionary..
# dict[3] = "hello"
# print(dict)

#Delete values inside dictionary..del, pop()
# del dict[3]  //just give the key no.
# print(dict)

# dict.pop(3)   //give the key no.
# print(dict)

# print(dict.popitem())  //prints the last key value pair being poped.

# print(dict.keys())
# print(dict.values())
# print(dict.items())

#    3. Tuples :=> tuples are similar to the lists just it is enclosed with the parenthesis.
#              tuple = (1,4,8)
#              print(tuple)

# Add data inside tuples :=> just concat it with another tuple.
# tuple1 = (2,4,6)
# tuple1 = tuple1 + (8,9,10)
# print(tuple1) 


#    4. Sets :=> An unordered collection of unique elements.
# set1 = {1,5,8,8}
# print(set1)


# Add ele in the set
# set1.add(9)
# print(set1)

# set2 = {11,12,14,5,1}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))  //common in both will be taken out and rem ele of set1 will be printed
# print(set1.symmetric_difference(set2)) //common in both will be taken out and rem ele of set1 and set2 will be printed
# B) =>  User Defined Data Structure
#     1. Array
#     2. Stack
#     3. Queue
#     4. Linked List
#     5. Tree
#     6. Graph



# Arguments in Python :=> Arguments are the inputs given to the function. We may pass these arguments from the function call to the function definition or we may not pass too.
### Types :
# 1) Required Argument :=> No of arguments should be same in both function call and fun def, also position/order should be same.
# def display(a,b):
#     print(a,b)
# display(10,20) 

# 2) Keyword Argument :=> Order or position is not required. Initialization will be done based on keywords(name).
# def display(a,b):
#     print(a,b)
# display(b=40, a=20)

#3) Default Argument :=> No of arguments need not be matched with both function call and function definition.
#                       Some of arguments will be consider as default arguments.
# def default(name, course="B.Tech"):
#     print(name)
#     print(course)
# default(name="abc", course="M.Tech")
# default(name="pqr")  #Even we don't give the value of course it will take its default value i.e "B.Tech"

#3) Variable Length Argument :=> Arbitary no of arguments...By placing * as a prefix to the argument of a function definition.
# def varLength(*courses):
#     for i in courses:
#         print(i)
# varLength("B.tech","M.tech","MBA","CA")
    

# a = 10//6
# print(a)

# b = 4*3.75 - 1
# print(b)


# def addition(a,b):
#     print(a+b)
# addition(4,5)

# def subtraction(a,b):
#     print(a-b)
# subtraction(6,7)

# def division(a,b):
#     print(a//b)
# division(10,2)

# def multiplication(a,b):
#     print(a*b)
# multiplication(2,3)



# a = 10
# a = str(a)
# print(type(a))


# c = "11"
# c = int(c)
# print(c)


# list : same as array in javascript.
# list1 = [2,4,2,5,6,6]
# def freq(list1):
#     Obj = {}
#     for i in list1:
#         if(Obj[i]):
#             Obj[i] += 1
#         else:
#             Obj[i] = 1
#     return Obj
# print(freq(list1))
 


# list1 = [2, 4, 2, 5, 6, 6]  

# def freq(list1):
#     obj = {}
#     for i in list1:
#         if i in obj:
#             obj[i] += 1
#         else:
#             obj[i] = 1
#     return obj

# print(freq(list1))



# list1 = [1,2,3,3,4,5,6,6],  # let arr = [1,2,3,3,4,5,6,6]
# for i in list1:             # for(let i=0; i<arr.length; i++){
#                              #          console.log(i)
#                             #        }
#     print(i)
       

# string = "Abccba"
# def checkPalindrome(string):
#     string = string.lower()
#     i = 0
#     j = len(string) - 1 

#     while i<j:
#         if string[i] == string[j]:
#             i+=1
#             j-=1
#         else:
#             return False
#     return True
# print(checkPalindrome(string)):


# list2 = [{"name": "abc", "age": 10}, {"name": "pqr", "age": 11}]
# for i in list2:
#     print(i["name"])



# tuple1 = (1,3,5,8)
# def freq(tuple1):
#     obj = {}
#     for i in tuple1:
#         if i in obj:
#             obj[i] += 1
#         else:
#             obj[i] = 1
#     return obj

# print(freq(tuple1))



# list1 = [2,4,1,5,8]   #append = push, pop=pop, reverse=reverse, sum=add all ele
#list1.append(7)      # remove ele at the start of list = pop(0)
#list1.pop()          # add ele at the start of list = insert(0,ele)
#list1.reverse()
#print(sum(list1))
#del list1[0]
#list1.pop(0)
# list1.insert(0,8)
# print(list1)


# generate a sequence of numbers from 0 to 9
# for i in range(10):
#     print(i)

# generate a sequence of numbers from 1 to 10 with a step of 2
# for i in range(1, 11, 2):   #range(start, stop, step)
#     print(i)

# convert the range object into a list
# my_list = list(range(5))
# print(my_list)  # outputs [0, 1, 2, 3, 4]


# list1 = list(range(1,31))
# print(list1)


# list1 = [1,2,3,4]
#list1 = list1[1:3]
#list1 = list1[::-1]
# print(list1)

# str = "abc"
# characters = list(str)
# print(characters)



# for n in range(2, 10):
#      for x in range(2, n):
#          if n % x == 0:
#              print(n, 'is not a prime no')
#              break
#          else:
#           print(n, 'is a prime number')
#           break


# for i in range(11):
#     if i%2 == 0:
#         print(i,'is an even no')
#         continue          # works like an else statement.
#     print(i,"an odd no")


# list1 = list(range(1,6))
# print(list1)

# a = [4,8]
# list2 = list(range(*a))
# print(list2)


# Lambda Expressions :=>
# add = lambda x, y: x + y
# print(add(3, 4))  # Output: 7


# square = lambda x: x**2
# print(square(5))  # Output: 25


# is_even = lambda x: x % 2 == 0
# print(is_even(4))  # Output: True
# print(is_even(5))  # Output: False


#List as stack =>
# stack1 = [1,3,5]
# stack1.append(7)
# stack1.append(8)
# # print(stack1)
# stack1.pop()
# print(stack1)



# A list in Python can be used as a queue data structure by using the built-in methods of the list. However, using a list as a queue can be inefficient in terms of performance because adding and removing elements from the beginning of the list can be a slow operation as it requires shifting all the remaining elements. In Python, the queue module provides a more efficient implementation of the queue data structure.
# That being said, here's an example of using a list as a queue:
# queue = []  # an empty list to act as the queue

# adding elements to the queue using the append() method
# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue)  # [10, 20, 30]

# removing elements from the queue using the pop() method with an index of 0
# item = queue.pop(0)
# print(item)   # 10
# print(queue)  # [20, 30]



#LIST Comprehension :=>
#List comprehension is a concise way of creating lists in Python. 
# It allows you to create a new list by applying an expression to each element in an existing list, 
# or by iterating over a sequence, and filtering the elements based on a condition.
# squares = [x**2 for x in range(10)]
# print(squares)   # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# even_nums = [x for x in range(10) if x % 2 == 0]
# print(even_nums)   # Output: [0, 2, 4, 6, 8]


#del statement :=>
# The del statement is used in Python to remove an item from a list or delete a variable from memory. 
# fruits = ['apple', 'banana', 'orange']
# del fruits[1]  # removes 'banana' from the list
# print(fruits)  # output: ['apple', 'orange']

# x = 5
# del x  # deletes the variable x from memory
# print(x)  # raises an error: NameError: name 'x' is not defined

# fruits = ['apple', 'banana', 'orange', 'pear', 'kiwi']
# del fruits[1:3]  # removes 'banana' and 'orange' from the list
# print(fruits)  # output: ['apple', 'pear', 'kiwi']

# person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# del person['age']  # removes the 'age' key-value pair from the dictionary
# print(person)  # output: {'name': 'Alice', 'city': 'New York'}


# x = 5
# y = 10
# z = 15
# del x, y, z  # deletes all three variables from memory
# print(x, y, z)  # raises an error: NameError: name 'x' is not defined
