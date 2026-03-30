# enumerate() gives index + value

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)  # index starts from 0

# Combine two lists together

names = ["Ali", "Ahmed", "Sara"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(name, "scored", mark)

# Loop through dictionary keys and values

student = {"name": "Ali", "age": 21, "grade": "A"}

for key, value in student.items():
    print(key, ":", value)

# Sort numbers in ascending order

numbers = [5, 2, 9, 1, 7]

for num in sorted(numbers):
    print(num)

# Loop in reverse order

nums = [1, 2, 3, 4, 5]

for num in reversed(nums):
    print(num)

# Combine multiple techniques

students = ["Ali", "Sara", "Ahmed"]
marks = [80, 90, 85]

# Sort students alphabetically and pair with marks
for i, (name, mark) in enumerate(sorted(zip(students, marks))):
    print(f"{i+1}. {name} -> {mark}")