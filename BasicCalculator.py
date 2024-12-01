5# Basic Calculator
def calculator():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operation = input("enter the operation(+, -, *, /):")
    if operation == '+':
        result = num1+num2
    elif operation == '-':
        result = num1-num2
    elif operation == '*':
        result = num1*num2
    elif operation == '/':
        if num2!=0:
            result = num1/num2
        else:
             result = "undefined( division by 0)"
    else:
        result = "invalid result"
    print("Result:",result)
calculator()

