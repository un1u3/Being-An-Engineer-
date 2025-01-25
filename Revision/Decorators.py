def outer_function(msg):
    message = msg
    
    def inner_function():
        print(message)
    return inner_function


# my_func = outer_function("HI")
# Bye = outer_function("bye")

# my_func() 
# Bye()


# Decorators 

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display fucntion Ran")


display()


import time

def timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
        
# hi = outer_function("Hi")
# bye = outer_function("BYe")
