def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
while True:
    choice = input("Enter Choice (1/2/3/4/):")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter a numbers.")
            continue
            
        if choice == '1':
            print(f"ResultL: {add(num1, num2)}")
        elif choice == '2':
            print(f"ResultL: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"ResultL: {multiply(num1, num2)}")
        else: 
            print(f"ResultL: {divide(num1, num2)}")