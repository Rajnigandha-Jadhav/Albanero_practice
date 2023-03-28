# PUBLIC and PRIVATE variables in Python :
# Public variables are accessible from anywhere in the code, while private variables are only accessible within the class where they are defined.

class Test:
    def __init__(self):
        self.var1 = 1 #public
        self_var1 = 11 #private

t = Test()
print(t.var1)



class Test:
    def __init__(self):
        self.var1 = 1 #public
        self._var1 = 11 #private
    def mytest(self):  #this class can be accessed publically
        print(self._var1)

t = Test()
print(t.var1)
t.mytest()



class Test:
    def __init__(self):
        self.var1 = 1 #public
        self._var1 = 11 #private
    def __mytest(self):  #this class can't be accessed publically anymore
        print(self._var1)

t = Test()
t.__mytest()