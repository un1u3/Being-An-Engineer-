# Notes 
''' 
The Python Random module is a built-in module fo generating random 
integers in Python. These numbers occur randomly adn does not follow 
any rules or instructions. We can therefore use this module to generate 
random numbers, disply random item for a list or string, adn so on.
'''
import random


# The Random Function 
num = random.random()
print(num)

# The randint function
num1 = random.randint(1,500)
print(num1)

# The randrange function 
num2 = random.randrange(1,10)
print(num2)

# The choice Funtion  
random_s = random.choice('Random Module') #a string  
print( random_s )  
random_l = random.choice([23, 54, 765, 23, 45, 45]) #a list  
print( random_l )  
random_s = random.choice((12, 64, 23, 54, 34)) #a set  
print( random_s )  

# The shuffele Function 

list1 = [34,23,65.86,23]

random.shuffle(list1)
random.shuffle(list1)
print(list1)



# Code Practical : Coding a siccsor paper game 
