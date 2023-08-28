# how to create an empty list

empty_list = []
print(empty_list)

# list of numbers

number_list = [1,2,3,4,5]

# list of strings

name_list = ['senthil', 'kumar']

# mutable or immutable ?  mutable

sample_list =  [1,2,3,4,5]
sample_list[1]= 10
print(sample_list)

# iterable or not?  iterable

for i in sample_list:
    print(i)

# ordered or unordered? ordered

for i in sample_list:
    print(i)

# min, max

cricket_score = [30,29,39,49,29]
print(max(cricket_score))
print(min(cricket_score))

# sort(ascending, descending)

cricket_score.sort()
print(cricket_score)

cricket_score.sort(reverse=True)
print(cricket_score)

# concatenate two list

sample_list1 = [1,2,3]
sample_list2 = [4,5,6]
print(sample_list1 + sample_list2)

sample_list1.extend(sample_list2)
print(sample_list1)

# adding elements to list

name_list = ['senthil', 'kumar']
name_list.append('praveen')
print(name_list)

name_list = ['senthil', 'kumar']
name_list.insert(1, 'praveen')
print(name_list)

# len of list

name_list = ['senthil', 'kumar', 'praveen', 'preetha']
print(len(name_list))

# slicing

name_list = ['senthil', 'kumar', 'praveen', 'preetha']
print(name_list[0])
print(name_list[-1])


print(name_list[0:3])
print(name_list[:])

print(name_list[-3])
print(name_list[-3:-1])

print(name_list[::4])



