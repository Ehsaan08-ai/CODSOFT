def calculator(operator, num1, num2):
    
    if operator == '+':
        result = num1 + num2
        print(f"Addition of num1 and num2 is: {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"Subtraction of num1 and num2 is: {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"Multiplication of num1 and num2 is: {result}")
    elif operator == '/':
        result = num1 / num2
        print(f"Division of num1 and num2 is: {result}")
    else:
        print("Invalid operator")

operator = input("Choose an operator + , - , * , / : ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calculator(operator, num1, num2) 