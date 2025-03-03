# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point.

a = float(input("Input first number: "))
b = float(input("Input second number: "))

if b != 0:
    print("Thr quotient is: ", a / b)
else:
    print("Division by zero is not allowed.")