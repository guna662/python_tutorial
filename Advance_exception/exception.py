
"""Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing. Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible."""
# with exception handling
n = 10
try:   # try block contain the code that might fail
    res = n / 0
except ZeroDivisionError:  # run the specific error which occurs in try block
    print("Can't be divided by zero!")

# Try without exception handling
# n=10
# res=n/0
# print(res)

"""
Difference Between Errors and Exceptions
Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).


# Syntax Error (Error)
print("Hello world"  # Missing closing parenthesis

# ZeroDivisionError (Exception)
n = 10
res = n / 0  """

# num=int(input("enter an number: "))
try: # try: Runs the risky code that might cause an error.
    num=int(input("enter an number: "))
    res = 100 / num
    
except ZeroDivisionError: # except: Catches and handles the error if one occurs.
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:  # else: Executes only if no exception occurs in try.
    print("Result is", res)
    
finally: # finally: Runs regardless of what happens useful for cleanup tasks like closing files.
    print("Execution complete.")

# 1. Catching Specific Exceptions
"""Catching specific exceptions makes code to respond to different exception types differently. It precisely makes your code safer and easier to debug. It avoids masking bugs by only reacting to the exact problems you expect.

Example: This code handles ValueError and ZeroDivisionError with different messages."""
try:
    x=int(input("enter the input: "))  # This will cause ValueError
    inv = 1 / x   # Inverse calculation
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")