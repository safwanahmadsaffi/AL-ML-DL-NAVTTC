# Create a dictionary
student = {
    "name": "Ali",
    "age": 22,
    "grade": "A"
}

# Access values
print(student["name"])
print(student.get("age"))

student = {"name": "Ali", "age": 22}

# Add new key
student["grade"] = "A"

# Update value
student["age"] = 23

print(student)

data = {"a": 1, "b": 2, "c": 3}

# Remove using pop
value = data.pop("b")

# Remove last inserted item
data.popitem()

print(data)
print("Removed:", value)

person = {"name": "Sara", "age": 25, "city": "Lahore"}

# Loop keys
for key in person:
    print(key, person[key])

# Loop items
for key, value in person.items():
    print(key, ":", value)

marks = {"Math": 85, "English": 78}

# Keys, values, items
print(marks.keys())
print(marks.values())
print(marks.items())

# Create dictionary of squares
squares = {x: x**2 for x in range(1, 6)}

print(squares)

# Count frequency of characters
text = "hello python"

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)