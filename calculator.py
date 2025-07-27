num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
#Asks user for operation
operation = input('Please type in operation [+,-,*,/]:')


if operation == '+':
    sum = num1 + num2
    print(f'The addition of {num1} and {num2} = {sum}')
elif operation == '-':
    sub = num1 - num2
    print(f'The subtraction of {num1} and {num2} = {sub}')
elif operation == '*':
    mul = num1 * num2
    print(f"The multiplication of {num1} and {num2} = {mul}")
elif operation == '/':
    div = num1 / num2
    print(f'The division of {num1} and {num2} = {div}')
else:
    print("Please Enter a valid operation!")