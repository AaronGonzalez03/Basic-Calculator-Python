print("=== BASIC CALCULATOR ===")
print("Available operations: add, subtract, multiply, divide")

operation = input("Enter the type of operation you want to perform: ").lower().strip()
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: You must enter valid numeric values")
    exit() 
result = None
if operation == "add" or operation == "+":
    result = num1 + num2
    symbol = "+"
elif operation == "subtract" or operation == "-":
    result = num1 - num2
    symbol = "-"
elif operation == "multiply" or operation == "*":
    result = num1 * num2
    symbol = "*"
elif operation == "divide" or operation == "/":
    if num2 != 0:
        result = num1 / num2
        symbol = "/"
    else:
        print("Error: Division by zero is not allowed")
        exit()
else:
    print(f"Error: '{operation}' is not a valid operation")
    exit() 
print("The result is:", result)