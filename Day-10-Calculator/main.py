# CALCULATOR PROGRAM
from art import logo




def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
     "+": add,
     "-": subtract,
     "*": multiply,
     "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?\n"))
    for operator in operations:
        print(operator)
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?\n"))
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        print(f"The result is : {num1} {operation} {num2} = {answer}")
        print(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")
        rep = input()
        if rep == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

