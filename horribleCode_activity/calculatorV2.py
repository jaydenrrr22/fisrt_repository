def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    choice = input("Enter the choice: (+, -, *, /): ")

    if choice == "+":
        print("Result is: ", a + b)
    elif choice == "-":
        print("Result is: ", a - b)
    elif choice == "*":
        print("Result is: ", a * b)
    elif choice == "/":
        print("Result is: ", a / b)
    else:
        print("Invalid input. Please try again.")

main()