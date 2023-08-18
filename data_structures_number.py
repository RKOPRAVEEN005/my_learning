# creating a number

var_1 = 1
print(var_1)
print(id(var_1))

var_2 = 2

print(var_2)
print(id(var_2))

var_3 = 1

print(var_3)
print(id(var_3))

# how to find type of a number?

print(type(1))
print(type(1.1))

# mutable or immutable?  immutable

var_4 = 10
try:
  var_4[1]= 1
except Exception as error:
    print('error from mutable or not? ' + str(error))

# iterable or not?  non iterable

try:
    for i in 10:
        print(i)
except Exception as error:
    print('error from iterable or not? ' + str(error))





