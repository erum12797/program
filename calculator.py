x = float(input("Enter X: "))
y = float(input("Enter Y: "))
op = input("Enter operation (+, -, *, /, **, %): ")

if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    print(x / y)
elif op == '**':
    print(x ** y)
elif op == '%':
    print(x % y)
else:
    print("Invalid operation")
