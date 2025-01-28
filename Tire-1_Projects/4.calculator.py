num1 = int(input("Enter a Number"))
operator = input("Enter (+,-,/,*)")
num2 = int(input("Enter a Number"))

match operator:
    case '+':
        print(f"{num1} {operator} {num2} =",num1 + num2)
    case '-':
        print(f"{num1} {operator} {num2} =",num1 - num2)
    case '*':
        print(f"{num1} {operator} {num2} =",num1 * num2)
    case '/':
        print(f"{num1} {operator} {num2} =",num1 / num2)
    case '%':
        print(f"{num1} {operator} {num2} =",num1 %  num2)
    case _:
        print("Invalid Input")