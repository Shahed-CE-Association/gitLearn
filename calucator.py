import sys
from operations import add, subtract, multiply, divide, power, modulus, square_root

def print_menu():
    entry = input("press any key to use magical calucator")
    if entry != " ":
        print("\n" + "=" * 40)
        print("       🧮 Advanced Python Calculator")
        print("=" * 40)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Modulus (%)")
        print("7. Square Root (√)")
        print("8. Exit")
        print("=" * 40)

def save_to_history(text):
    try:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
    except Exception:
        pass

def main():
    print("Welcome to the Git Workshop Calculator!")
    
    while True:
        print_menu()
        choice = input("Please select an option (1-8): ").strip()

        if choice == '8':
            print("Exiting application. Have a great day!")
            sys.exit()

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                number1 = float(input("Enter the first number: "))
                number2 = float(input("Enter the second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")
                continue

            result = None
            if choice == '1':
                result = add(number1, number2)
                op_str = f"{number1} + {number2} = {result}"
            elif choice == '2':
                result = subtract(number1, number2)
                op_str = f"{number1} - {number2} = {result}"
            elif choice == '3':
                result = multiply(number1, number2)
                op_str = f"{number1} * {number2} = {result}"
            elif choice == '4':
                result = divide(number1, number2)
                op_str = f"{number1} / {number2} = {result}"
            elif choice == '5':
                result = power(number1, number2)
                op_str = f"{number1} ^ {number2} = {result}"
            elif choice == '6':
                result = modulus(number1, number2)
                op_str = f"{number1} % {number2} = {result}"

            print(f"✅ Result: {result}")
            save_to_history(op_str)

        elif choice == '7':
            try:
                number1 = float(input("Enter the number for square root: "))
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
                continue

            result = square_root(number1)
            op_str = f"sqrt({number1}) = {result}"
            print(f"✅ Result: {result}")
            save_to_history(op_str)
        else:
            print("❌ Invalid choice! Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()  