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
#         => del : 
#del list[2]
#print(list)
#         => pop()
#         => remove()
#    2. Dictionary
#    3. Tuples
#    4. Sets

# B) =>  User Defined Data Structure
#     1. Array
#     2. Stack
#     3. Queue
#     4. Linked List
#     5. Tree
#     6. Graph
