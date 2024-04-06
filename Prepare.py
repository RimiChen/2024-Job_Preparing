print(range(10))


# a line comment
"""
Test the comment
for two lines
"""
for i in range(3):
    if (i < 2):
        print(i)
    else:
        print(i, end=" ")
        print(" add" , "an", "end", sep="_" )

#-----
loop_array = ["test1", "test2", "test3"]
for item in loop_array:
    print(item)

#-----
count = 0
while (count < 3):
    count = count + 1
    print("Test count ", count)

#-----
List = [char for char in [1, 2, 3]]
print(List)

#-----
Dict = {1:'first', 2:'second', 3:'thrid'}
print(Dict)

#-----
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

myDict = { k:v for (k,v) in zip(keys, values)}
myDict_2 = dict(zip(keys, values))

print(myDict)
print(myDict_2)

#-----tuple
tuple_var = ("tuple", "element1", "element2", "more than three")
print(tuple_var)

#-----map
def testFun(x, y):
    return x + y -1

numbers = (1, 2, 3, 4)
numbers2 = (8, 10, 13, 15)
result = map(testFun, numbers, numbers2)
print(list(result))

#-----Reduce
from functools import reduce

nums = [5, 7, 3, 4]
ans = reduce(lambda x, y: x + y, nums)

print(ans)

#-----
a = [1, 2, 5] 
try: 
    print ("Second element = %d" %(a[1])) 
  
    # Throws error since there are only 3 elements in array 
    print ("Fourth element = %d" %(a[3])) 
  
except: 
    print ("An error occurred") 


#-----Class
class Car:
    def __init__(self, make, model, year):
        self._make = make #  protected
        self.__model = model # private
        self.year = year # public attribute
    def get_make(self):
        return self._make
    def set_model(self):
        self.__model = model
    def get_model(self):
        return self.__model

test_car = Car("Toshiba", "Unknown", 2024)