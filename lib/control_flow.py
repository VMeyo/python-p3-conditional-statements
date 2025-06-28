# 1. Functions that checks username and password.

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
        # Checks for username 'admin'/'ADMIN' and password '12345'
        return "Access granted" # If condition is true
    else:
        return "Access denied" # If condition is false
    
# 2. Function that checks weather temperature.

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!" # Return value for temperatures below 40
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!" # Return value for temperatures between 40 and 65
    elif temperature > 85:
        return "It's too dang hot out there!" # Return value for temperatures above 85
    else:
        return "It's perfect out there!"

# 3. Function that checks on multiples of 3 & 5     

def fizzbuzz(num): # Quotient operator used to check on the remainder
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz" # Return value for multiples of both 3 & 5
    elif num % 3 == 0:
        return "Fizz" # Return value for multiples of 3
    elif num % 5 == 0:
        return "Buzz" # Return value for multiples of 5
    else:
        return num # Return value for any other number
    

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

    
