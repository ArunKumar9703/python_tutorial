# This is a simple calculator program that performs basic arithmetic operations.
# The program defines functions for addition
def add_numbers(a, b):
    return a + b
def subtract_numbers(a, b):
    return a - b
# The program defines functions for multiplication
def multiply_numbers(a, b):
    return a * b    
# The program defines functions for division
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
# The program prompts the user to select an operation and input two numbers
print("This select Operation:"
      "1. Addition\n",
      "2. Subtraction\n",
      "3. Multiplication\n",
      "4. Division\n")
# The program takes user input for the operation and numbers, performs the selected operation, and displays the result
# The Selection1 variable is 1 addition, 2 subtraction, 3 multiplication, and 4 division
selection1 = input("Select an operation (1/2/3/4):\n ")
# The program takes user input for two numbers
n1= int(input("Enter first number: "))
n2= int(input("Enter second number: "))

# If Selection1 is 1, the program performs addition and displays the result
if selection1 == '1':
    print(n1, "+", n2, "=", add_numbers(n1, n2))
# If Selection1 is 2, the program performs subtraction and displays the result
elif selection1 == '2':
    print(n1, "-", n2, "=", subtract_numbers(n1, n2))
# If Selection1 is 3, the program performs multiplication and displays the result
elif selection1 == '3':
    print(n1, "*", n2, "=", multiply_numbers(n1, n2))
# If Selection1 is 4, the program performs division and displays the result
elif selection1 == '4':
    print(n1, "/", n2, "=", divide_numbers(n1, n2))
else:
    print("Invalid input")