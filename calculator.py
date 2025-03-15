# Basic calculator program

# Get user input for the first number, second number and operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation: ")

# Perform the operation based on the user's choice
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check if the second number is zero to avoid division by zero error
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = num1 / num2
else:
    result = "No numbers provided"
    
print(f"{num1} {operation} {num2} = {result}")            