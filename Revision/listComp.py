nums = [1,2,3,4,5,6,6]

# my_list = []
# for n in nums:
#     my_list.append(n)

# my_list =  [n for n in nums]


# my_list = []
# for n in nums:
#     my_list.append(n*n)

# my_list =  [n for n in nums]


# my_list = [n*n for n in nums ]
# print (my_list)


# myList = [n **n for n in nums]

# print(myList)

# my_list = [n for n in nums if n %2 == 0]
# print(my_list)




# myList = []

# for letter in 'abcd':
#     for num in range(4):
#         myList.append((letter,num))

# print(myList)

# myList = [ (letter,num) for letter in 'adcd' for num in range(4)]

# print(myList)



# Dictonary Example 

# names = ['hari','ram']
# heros = ['Batman','Ironman']


# myDict = {}

# for name, hero in zip(names,heros):
#     myDict[name] = hero 

# print(myDict)

# my_dict = {name: hero for name, hero in zip(names,heros)}
# print(my_dict)



# set Comprehensions
# nums = [1,2,3,3,4,4,5]
# my_set = set()

# for n in nums:
#     my_set.add(n)

# print(my_set)


# Generator Expressions 

nums = [1,2,3,4,5]

# def gen_func(nums):
#     for n in nums:
#         yield n * n 

# my_gen = gen_func(nums)

# for i in my_gen:
#     print(i)


gen  = ( n*n for n in nums)

for i in gen:
    print(gen)