firstNum = input("Enter first number: ")
firstNum = int(firstNum)

secondNum = input("Enter second number: ")
secondNum = int(secondNum)

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(firstNum + secondNum)
elif operation == "-":
    print(firstNum - secondNum)
elif operation == "*":
    print(firstNum * secondNum)
elif operation == "/":
    print(firstNum / secondNum)
else:
    print("Invalid Operation")
