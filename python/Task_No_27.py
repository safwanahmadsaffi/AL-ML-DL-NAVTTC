class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    
    if age < 18:
        raise AgeError("You are not eligible to vote.")
    
    print("You can vote!")

except AgeError as e:
    print("Error:", e)

class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message

try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    
    print("Valid number:", num)

except NegativeNumberError as e:
    print("Error:", e.message)

class TooSmallError(Exception):
    pass

class TooLargeError(Exception):
    pass

try:
    num = int(input("Enter a number between 1 and 100: "))
    
    if num < 1:
        raise TooSmallError("Number is too small.")
    elif num > 100:
        raise TooLargeError("Number is too large.")
    
    print("Valid input!")

except TooSmallError as e:
    print("Error:", e)
except TooLargeError as e:
    print("Error:", e)

class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance.")
    return balance - amount

try:
    bal = 5000
    amt = int(input("Enter withdrawal amount: "))
    
    bal = withdraw(bal, amt)
    print("Remaining balance:", bal)

except InsufficientBalanceError as e:
    print("Error:", e)

class InvalidPasswordError(Exception):
    pass

try:
    password = input("Enter password: ")
    
    if len(password) < 6:
        raise InvalidPasswordError("Password must be at least 6 characters long.")
    
    print("Password accepted!")

except InvalidPasswordError as e:
    print("Error:", e)

finally:
    print("Password check completed.")

class MarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))
    
    if marks < 0 or marks > 100:
        raise MarksError("Marks must be between 0 and 100.")
    
    print("Marks are valid.")

except MarksError as e:
    print("Error:", e)