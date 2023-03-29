name = "Pari"
age = 20
sal = 35000.50

# Approach 1 :=>
print(name,age,sal)

# Approach 2 :=>
print("Name is:", name)
print("Age is:", age)
print("Sal is:", sal)


# Approach 3 :=>Using % operator, here type is important
print("Name:%s Age:%d Salary:%g" % (name,age,sal))


# Approach 4 :=>using {}, here value is imp
print("Name:{} Age:{} Salary:{}".format(name,age,sal))


# Approach 5 :=>using {}, here index and value is imp
print("Name:{0} Age:{1} Salary:{2}".format(name,age,sal))

