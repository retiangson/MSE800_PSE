"""
This project demonstrates how to use a Python decorator to measure
a function’s execution time.

Decorators are useful when we want to execute extra logic BEFORE and AFTER a function runs,
without modifying the function’s internal code.

In this example, we use the decorator to:
1. Record the start time before the function executes.
2. Call the target function (which uses time.sleep() to simulate a process delay).
3. Record the end time after the function executes.
4. Print how long the function took to complete.

We use decorators because they:
- Promote code reusability (we can apply the same timing logic to many functions).
- Reduce duplication (no need to write timing code inside every function).
- Improve maintainability (cross-cutting concerns like logging or timing live in one place).
- Keep our functions clean and focused on their main purpose.

We should use decorators when:
We need consistent behavior (like logging, authentication, or timing) across multiple functions.
We want to execute setup or cleanup logic automatically around function calls.
We want to add functionality without altering the original function's implementation.
"""

import time

# -----------------------------------------------------------------------------
# execution_timer decorator
# -----------------------------------------------------------------------------
# This decorator measures how long a function takes to execute.
# It runs BEFORE and AFTER the function, just like an Action Filter in C#.
# -----------------------------------------------------------------------------
def execution_timer(func):
    def wrapper(*args, **kwargs):
        #BEFORE the main function
        start_time = time.time()
        print(f"Starting '{func.__name__}' with arguments {args}, {kwargs}")

        # Call the original function (which may take some time)
        result = func(*args, **kwargs)

        #AFTER the main function
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"'{func.__name__}' completed in {elapsed:.2f} seconds")

        return result

    return wrapper


# -----------------------------------------------------------------------------
# Example Function
# -----------------------------------------------------------------------------
# The '@execution_timer' decorator wraps this function and automatically measures
# how long it takes to execute.
#
# Using 'time.sleep()' simulates a time-consuming operation such as
# file processing, API calls, or database queries.
# -----------------------------------------------------------------------------
@execution_timer
def process_data():
    print("Processing data...")
    time.sleep(2)  # Simulate a 2-second task
    print("Data processed successfully!")
    return "OK"


# -----------------------------------------------------------------------------
# Program Execution
# -----------------------------------------------------------------------------
# When 'process_data()' is called, it doesn't execute directly.
# The decorator first logs the start, measures the duration,
# and prints the total execution time after completion.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    process_data()
