# how to identify a string
var_1 = "sample"
print(type(var_1))

# string is mutable or not?  immutable

try:
  var_1[0]= 'T'
except Exception as error:
    print('error from mutable or not? ' + str(error))

# iterable or not? iterable

for i in var_1:
    print(i)

# ordered or not? ordered

for i in var_1:
    print(i)

 # concatanate two strings

result =  'senthil' + 'kumar'
print(result)

# multiply with *

result = 'kumar ' * 5
print(result)

# Upper, lower, capital method

print('senthil'.upper())
print('SENTHIL'.lower())
print('senthil'.capitalize())

# strip white space
print('    senthil')
print('    senthil'.strip())

# split

print('senthil'.split('t'))




