# =====================================
# 🖩 PYTHON CALCULATOR - INPUT VALIDATION & ERROR HANDLING
# =====================================

history = []

print("Welcome to the Python CLI Calculator!")
print("Type 'history' to see past calculations or 'exit' to quit.\n")

while True:
    # ✅ VALIDATE FIRST NUMBER
    while True:
        try:
            first_num = float(input("Enter first number: ").strip())
            break
        except ValueError:
            print('❌ Not a valid number! Try again.')

    # ✅ VALIDATE OPERATOR
    operator = input("Enter operator (+,-,*,/): ").strip()
    while operator not in '+-*/':
        print('❌ Not a valid operator! Try again.')
        operator = input("Enter operator (+,-,*,/): ").strip()

    # ✅ VALIDATE SECOND NUMBER & PREVENT DIVISION BY ZERO
    while True:
        try:
            second_num = float(input("Enter second number: ").strip())
            if operator == '/' and second_num == 0:
                print('❌ Cannot divide by zero! Try again.')
                continue
            break
        except ValueError:
            print('❌ Not a valid number! Try again.')

    # ✅ PERFORM CALCULATION
    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    elif operator == '/':
        result = first_num / second_num

    # ✅ STORE & DISPLAY RESULT
    solution = f"{first_num} {operator} {second_num} = {result}"
    history.append(solution)
    print(f"\n✅ Calculation: {solution}")

    # ✅ USER MENU (Continue, History, Exit)
    while True:
        choice = input("\nWould you like to perform another calculation? (yes/no/history/exit): ").strip().lower()
        if choice == 'yes':
            break
        elif choice == 'history':
            print("\n📜 Calculation History:")
            for entry in history:
                print(entry)
        elif choice == 'exit' or choice == 'no':
            print("👋 Thanks for using our calculator!")
            exit()
        else:
            print("❌ Not a valid input, please try again.")
        
        # =====================================
# 🖩 PYTHON CALCULATOR - VALIDATION & ERROR HANDLING
# =====================================

# ✅ IMPORT REUSABLE VALIDATION FUNCTIONS
from ControlFlow import get_number
from Functions_And_Scope import operations

# ✅ GET USER INPUT WITH VALIDATION
num1 = get_number("Enter first number: ")
operation = input("Enter operator (+, -, *, /, ^): ").strip()
while operation not in operations:
    print("❌ Invalid operator!")
    operation = input("Enter a valid operator (+, -, *, /, ^): ").strip()
num2 = get_number("Enter second number: ")

# ✅ PERFORM CALCULATION
result = operations[operation](num1, num2)
print(f"✅ Result: {num1} {operation} {num2} = {result}")

# 🔹 **For deeper understanding of input validation, see `ControlFlow.py`**    

# 🔹 **This calculator demonstrates key exception handling concepts.**
# **For a deep dive into exception handling, see `ControlFlow.py`.**


class Calculator:
    def __init__(self):
        self.history = []
        self.valid_operators = ['+', '-', '*', '/', '^']

    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Not a valid number, please try again.")

    def get_operator(self):
        while True:
            operator = input(f"Enter operation ({', '.join(self.valid_operators)}): ").strip()
            if operator in self.valid_operators:
                return operator
            print("Invalid operator! Try again.")

    def perform_operation(self, num1, operation, num2):
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Error: Cannot divide by zero!",
            '^': lambda x, y: x ** y,
        }
        return operations[operation](num1, num2)

    def format_result(self, result):
        return f"{result:.2f}" if isinstance(result, float) else result

    def add_to_history(self, calculation):
        self.history.append(calculation)

    def show_history(self):
        print("\nCalculation History:")
        for calc in self.history:
            print(calc)

    def run(self):
        while True:
            num1 = self.get_number("Enter first number: ")
            operator = self.get_operator()
            num2 = self.get_number("Enter second number: ")

            result = self.perform_operation(num1, operator, num2)
            formatted_result = self.format_result(result)
            calculation = f"{num1} {operator} {num2} = {formatted_result}"

            self.add_to_history(calculation)
            print(f"Result: {calculation}")

            choice = input("Would you like to calculate again? (y/n/history): ").strip().lower()
            if choice == 'history':
                self.show_history()
            elif choice == 'n':
                print("Thanks for using the calculator!")
                break