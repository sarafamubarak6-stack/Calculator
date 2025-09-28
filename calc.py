def Add(x, y):
    return x + y
def Subtract(x, y):
    return x - y
def Multiply(x, y):
    return x * y
def Divide(x, y):
    if y == 0:
        return"Error: Cannot divide by zero"
    return x / y
print("Select aperation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice from 1-4: ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result:", Add(num1, num2))
elif choice == "2":
    print("Result:", Subtract(num1, num2))
elif choice == "3":
    print("Result:", Multiply(num1, num2))
elif choice == "4":
    print("Result:", Divide(num1, num2))
else:
    print("Invalid input")