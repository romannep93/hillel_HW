operation = ['+', '-', '/', '*']
a = float(input('Enter the first number:'))
b = str(input('Specify the operation (+, -, *, /):'))
c = float(input('Enter the second number:'))
if b == '/' and c == 0:
    print('Division by 0 is not allowed')
elif b not in operation:
    print('Check "operation" input field')
elif b == '/':
    print(a / c)
elif b == '*':
    print(a * c)
elif b == '+':
    print(a + c)
elif b == '-':
    print(a - c)
