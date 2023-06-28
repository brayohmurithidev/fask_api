'''
A decorator enhances a fn functionality without modifying the fn, method
or class directly.
They are created using @ and take in the target fn as the argument. & returns
modified or wrapped version of the target fn
'''


def my_decorator(func):
    '''A wrapper fn that wraps the target function'''
    def wrapper(*args, **kwargs):
        # BEHAVIOR BEFORE TARGET FN
        print("Before fn execution")

        # Call the target fn
        result = func(*args, **kwargs)

        # Behavior after fn is called
        print("After fn execution")

        return result
    return wrapper


# Function
@my_decorator
def my_function():
    print("Inside the function")


# call the function
my_function()
