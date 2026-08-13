def calculator():
    print("--- Simple Python Calculator ---")
    print("Available Operations:")
    print("  +  for Addition")
    print("  -  for Subtraction")
    print("  *  for Multiplication")
    print("  /  for Division")
    
    # Prompt user for the operation
    operation = input("\nEnter your operation choice (+, -, *, /): ")
    
    # Check if the operation is valid
    if operation in ('+', '-', '*', '/'):
        try:
            # Prompt user for the two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            return

        # Perform the calculation based on the chosen operation
        if operation == '+':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
            
        elif operation == '-':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
            
        elif operation == '*':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
            
        elif operation == '/':
            if num2 == 0:
                print("\nError: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation entered. Please choose from +, -, *, or /.")

# Run the calculator
if __name__ == "__main__":
    calculator()
