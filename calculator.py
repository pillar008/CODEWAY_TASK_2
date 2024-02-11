# addition
def add(x, y):
    return x + y

# subtraction
def subtract(x, y):
    return x - y

# multiplication
def multiply(x, y):
    return x * y

# division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Welcome to Simple Calculator")

# input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# options 
print("Available operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter operation number (1/2/3/4): ")

# Logic
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
