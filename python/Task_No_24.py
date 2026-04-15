# Create a set
nums = {1, 2, 3, 4, 4, 5}

print(nums)   # Duplicate 4 will be removed

fruits = {"apple", "banana", "cherry"}

# Add elements
fruits.add("mango")

# Remove elements
fruits.remove("banana")   # Error if not found
fruits.discard("grapes")  # No error if not found

print(fruits)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union
print(A & B)   # Intersection
print(A - B)   # Difference

colors = {"red", "green", "blue"}

for color in colors:
    print(color)

numbers = {10, 20, 30, 40}

if 20 in numbers:
    print("20 exists in set")

if 50 not in numbers:
    print("50 not found")

# Create a set of squares
squares = {x**2 for x in range(1, 6)}

# Even numbers only
evens = {x for x in range(1, 11) if x % 2 == 0}

print(squares)
print(evens)

# Remove duplicates from a list using set
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print("Original:", numbers)
print("Unique:", unique_numbers)