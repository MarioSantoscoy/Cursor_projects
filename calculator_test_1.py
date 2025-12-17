# Make a calculator that can add, subtract, multiply and divide two numbers
# Then, executes the operation and shows the result
# It must repeat the process until the user writes "exit"

# The following functions perform basic arithmetic operations for a calculator:
# add(num1, num2): returns the sum of num1 and num2.
# rest(num1, num2): returns the result of num1 minus num2.
# multiply(num1, num2): returns the product of num1 and num2.
# divide(num1, num2): divides num1 by num2 and prints the result as an integer, raises error if num2 > num1
# exit(): prints a thank you message for using the calculator.

def add(num1, num2):
    print(num1 + num2)

def rest(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    if num2 > num1:
        raise ValueError("The first number must be greater than second number")
    else:
        print(int(num1 / num2))

def exit():
    print("Thank you for using the calculator")

# The following code is a simple calculator that can add, subtract, multiply and divide two numbers.
# It repeats the process until the user writes "exit".
# It uses the functions defined above to perform the operations.
# It prints a thank you message for using the calculator before exiting program.


while True:
    operation = input("Enter the operation: ")
    if operation == "exit":
        print("Thank you for using the calculator")
        break
    else:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid number")
            continue
        if operation == "add":
            add(num1, num2)
        elif operation == "rest":
            rest(num1, num2)
        elif operation == "multiply":
            multiply(num1, num2)
        elif operation == "divide":
            divide(num1, num2)
        else:
            print("Invalid operation")


