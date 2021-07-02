
firstNumber = input("Type your first number: ")
secondNumber = input("Type your second number")

while firstNumber.isalpha() or secondNumber.isalpha():
    print("Please, type a number not a letter/name")
    firstNumber = input("Type your first number: ")
    secondNumber = input("Type your second number")

print("Thank you")
firstNumber = float(firstNumber)
secondNumber = float(secondNumber)
Action = input("Type the mathematical symbol for action with your numbers(+ or - or * or / : ")

if Action == "+":
    Result = firstNumber + secondNumber
    print(Result)
elif Action == "-":
    Result = firstNumber - secondNumber
    print(Result)
elif Action == "*":
    Result = firstNumber * secondNumber
    print(Result)
elif Action == "/":
    Result = firstNumber / secondNumber
    print(Result)
else:
    print("The mathematical action you have typed is wrong. Try again.")


