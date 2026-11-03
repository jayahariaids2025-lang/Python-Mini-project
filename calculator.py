
# Python Mini Project - Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b


def power(a, b):
    return a ** b


def calculator():

    while True:

        print("\n================================")
        print("       PYTHON CALCULATOR")
        print("================================")

        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "7":
            print("Thank you for using Python Calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice! Please select 1-7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                result = divide(num1, num2)

            elif choice == "5":
                result = modulus(num1, num2)

            elif choice == "6":
                result = power(num1, num2)

            print("\nResult:", result)

        except ValueError:
            print("Invalid input! Please enter numeric values.")


# Start the calculator
if __name__ == "__main__":
    calculator()
