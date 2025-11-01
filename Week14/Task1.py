# This decorator is used to wrap another function and execute additional logic
# BEFORE and AFTER the target function runs — very similar in concept to
# an Action Filter in ASP.NET MVC (C#), which can intercept controller actions
# to perform tasks such as logging, authentication, or validation.

def log_decorator(func):
    # 'func' is the target function that will be wrapped
    def wrapper(*args, **kwargs):
        # Executes BEFORE the main function
        # Here, we log the function name and arguments
        print(f"Calling {func.__name__} with {args}, {kwargs}")

        # Call the original function and store its result
        result = func(*args, **kwargs)

        # Executes AFTER the main function
        # We log the return value for debugging or monitoring
        print(f"{func.__name__} returned {result}")

        # Return the result so normal function behavior continues
        return result

    # Return the wrapper function to replace the original one
    return wrapper


# The '@log_decorator' syntax is Python’s way of attaching the decorator.
# It automatically wraps the 'add' function with 'log_decorator'.
@log_decorator
def add(a, b):
    # A simple function to demonstrate the decorator in action
    return a + b


# When you call 'add(3, 5)', it doesn't directly execute 'add'.
# Instead, it first runs 'wrapper()', which adds logging before and after the call.
add(3, 5)
