print(type(4.5))


var_4=5
print(id(var_4))

var_5=5
print(var_5)
print(id(var_5))

num=10
try:
 num[2]=1
except Exception as error:
 print("number is immutable")
