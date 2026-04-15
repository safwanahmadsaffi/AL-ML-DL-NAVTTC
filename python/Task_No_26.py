try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ValueError:
    print("Invalid input! Enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x + y

except ValueError:
    print("Invalid input!")

else:
    print("Sum is:", result)

finally:
    print("Execution completed.")

def check_age(age):
    if age < 18:
        raise Exception("You must be 18 or older.")
    else:
        print("Access granted.")

try:
    age = int(input("Enter your age: "))
    check_age(age)

except Exception as e:
    print("Error:", e)

try:
    x = int("abc")
except Exception as e:
    print("Something went wrong:", e)