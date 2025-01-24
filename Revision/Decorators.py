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


def display():
    print("Display fucntion Ran")
    
decorated_display = decorator_function(display)

decorated_display()

# hi = outer_function("Hi")
# bye = outer_function("BYe")
