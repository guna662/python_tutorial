#  ⿡ INT – Whole Number

# Use case: Counting students, tickets, or likes.

# Example 1: Counting students in a class
students = 35
new_students = 5
total_students = students + new_students
print("Total students:", total_students)

# Example 2: Likes on a post
likes = 120
dislikes = 20
print("Net likes:", likes - dislikes)


# 2. Float = numbers with decimals or fractions.

# Use case: Handling money, marks, temperature, or averages.

# Example 1: Temperature
temperature = 36.8
print("Body temperature:", temperature, "°C")

# Example 2: Average marks
math = 85.5
science = 90.0
english = 88.5
average = (math + science + english) / 3
print("Average Marks:", average)


# #3.String: 
# Use case: Names, messages, sentences, or any text.
# Example 1: Greeting message
name = "Asha"
print("Hello,", name)

# Example 2: Combine text and numbers
age = 16
print(f"{name} is {age} years old.")

# Example 3: Text operations
quote = "Python is fun!"
print("Uppercase:", quote.upper())
print("Number of letters:", len(quote))


# ⿤ BOOLEAN – The Truth Teller

# Use case: Checking if something is True or False (used in logic & decisions).

# Example 1: Exam result
score = 45
passed = score >= 35
print("Passed?", passed)

# Example 2: Login system
is_logged_in = False
if not is_logged_in:
    print("Please log in first.")

# ⿥ LIST – The Organizer

# Use case: Storing multiple items (e.g., student names, prices).

# Example 1: Shopping list
shopping = ["milk", "bread", "eggs"]
print("Shopping list:", shopping)

# Example 2: Add new item
shopping.append("butter")
print("Updated list:", shopping)

# Example 3: Loop through list
for item in shopping:
    print("Buy:", item)

# 🧠 List = group of items that can be changed (add, remove, etc.).

# ⿦ TUPLE – The Locked Basket

# Use case: Store fixed data like coordinates or fixed student details.

# Example 1: Location coordinates
coordinates = (12.9716, 77.5946)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# Example 2: Immutable (cannot change)
# coordinates[0] = 13.0  ❌ will cause error


# 🧠 Tuple = collection you can’t modify.

# ⿧ DICTIONARY – The Smart Librarian

# Use case: Store key-value data like student info, product details.

# Example 1: Student information
student = {
    "name": "Ravi",
    "age": 15,
    "marks": 92,
    "passed": True
}
print(student["name"], "scored", student["marks"])

# Example 2: Update info
student["age"] = 16
print("Updated age:", student["age"])

# 🧠 Dictionary = data stored as “key: value”.

# ⿨ SET – The Unique Collector

# Use case: Remove duplicates or find unique items.

# Example 1: Unique student IDs
student_ids = {101, 102, 103, 101, 102}
print("Unique IDs:", student_ids)

# Example 2: Finding common elements
math = {"Ravi", "Asha", "Maya"}
science = {"Asha", "Kiran", "Ravi"}
print("Students taking both:", math.intersection(science))


# 🧠 Set = unique values only (no duplicates).
