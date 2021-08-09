#Calculator
from art import logo

print(logo)

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
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    #Here we select "+"
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    previous_result = first_answer
    continue_calculating = "y"

    while continue_calculating != "n":
        continue_calculating = input(f"Type 'y' to continue calculating with {previous_result}, or type 'n' to start a new calculation ")

        if continue_calculating != "n":
            operation_symbol = input("Pick an operation: ") 
            numx = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol] 
            next_answer = calculation_function(previous_result, numx)
            print(f"{previous_result} {operation_symbol} {numx} = {next_answer}")
            previous_result = next_answer
        else:
            calculator()

calculator()