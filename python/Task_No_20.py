# Function with no parameters
def greet():
    print("Hello, Welcome to Python!")

greet()  # Function call

# Function that takes input parameter
def greet_user(name):
    print("Hello,", name)

greet_user("Ali")
greet_user("Sara")

# Return multiple values (sum and average)
def calculate_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg  # Returning two values

nums = [10, 20, 30, 40]

s, a = calculate_stats(nums)
print("Sum:", s)
print("Average:", a)