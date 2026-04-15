# Create a string
text = "Hello World"

# Access characters
print(text[0])     # First character
print(text[-1])    # Last character

# Slicing
print(text[0:5])   # "Hello"

first = "Hello"
second = "Python"

# Concatenation
result = first + " " + second

# Repetition
repeat = first * 3

print(result)
print(repeat)

text = "Python Programming"

print(text.upper())        # Convert to uppercase
print(text.lower())        # Convert to lowercase
print(text.replace("Python", "Java"))

word = "Code"

# Loop through characters
for ch in word:
    print(ch)

# Using index
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")

data = "Python123"

print(data.isalpha())   # Only letters?
print(data.isdigit())   # Only digits?
print(data.isalnum())   # Letters + numbers?

text = "Python"

# Using slicing
reverse = text[::-1]

print("Original:", text)
print("Reversed:", reverse)

# Count vowels in a string
text = "Hello Python Programming"
vowels = "aeiouAEIOU"

count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)