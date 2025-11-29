print("-----Catching Multiple Exceptions--------")
a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")

print("-----------Catch-All Handlers and Their Risks____")

try:
    res = "100" / 20 # Risky operation: dividing string by number
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")

print("--------- Raise an Exception------------")
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)

print("--------Custom Exceptions--------")

class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except AgeError as e:
    print(e)