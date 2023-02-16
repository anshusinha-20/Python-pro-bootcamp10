import calculator
import os

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2


def calc():

    print(calculator.logo)

    firstNum = float(input("What's the first number?: "))

    print("""
        +
        -
        *
        /
    """)

    endOfCalculator = False

    while (endOfCalculator == False):

        operator = input("Pick an operation: ")

        secondNum = float(input("What's the next number?: "))

        if (operator == "+"):
            result = add(firstNum, secondNum)
        elif (operator == "-"):
            result = sub(firstNum, secondNum)
        elif (operator == "*"):
            result = mul(firstNum, secondNum)
        elif (operator == "/"):
            result = div(firstNum, secondNum)

        print(f"{firstNum} {operator} {secondNum} = {result}")

        continueCalculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if (continueCalculating == 'y'):
            firstNum = result
        elif (continueCalculating == 'n'):
            endOfCalculator = True
            os.system("clear")
            calc()
        else:
            print("Wrong input. Program terminated!")
            endOfCalculator = True
      
calc()
    



