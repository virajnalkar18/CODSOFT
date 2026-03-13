def calculator():
    print("=== SIMPLE CALCULATOR ===")
    print("Operations: +, -, *, /, ** (power), % (modulo)")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            # Get user input
            num1 = input("Enter first number: ")
            if num1.lower() == 'quit':
                print("Goodbye!")
                break
                
            num2 = input("Enter second number: ")
            if num2.lower() == 'quit':
                print("Goodbye!")
                break
                
            operation = input("Enter operation (+, -, *, /, **, %): ")
            
            # Convert to float
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform calculation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            elif operation == '%':
                if num2 == 0:
                    print("Error: Modulo by zero!")
                    continue
                result = num1 % num2
            else:
                print("Invalid operation! Please use +, -, *, /, **, or %")
                continue
            
            # Display result
            print(f"Result: {num1} {operation} {num2} = {result}")
            print("-" * 30)
            
        except ValueError:
            print("Error: Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()
