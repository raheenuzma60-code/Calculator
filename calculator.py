def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
        return
    return a / b


# User Input
print("___calculator___")
first_num = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
second_num = float(input("Enter the second number: "))

# Function Calling
if operator == "+":
    result = add(first_num, second_num)

elif operator == "-":
    result = subtract(first_num, second_num)

elif operator == "*":
    result = multiply(first_num, second_num)

elif operator == "/":
    result = divide(first_num, second_num)

else:
    result = "Invalid Operator!"

print("Result:", result)