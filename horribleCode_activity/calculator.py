#add function will take two parameters a and b
#and it will return a + b
def add(a, b):
    return a + b

#sub function takes two parameters a and b
#and it will return a - b
def sub(a, b):
    return a - b

#mul function takes two parameters a and b,
#and it will return a * b
def mul(a, b):
    return a * b

#div function takes two parameters a and b,
#and it will return a / b
def div(a, b):
    return a / b

#calculator function is the main function and will take user input
#based on which operation user chose this will do calculation
def calculator():
    print("Simple Calculator")

    #asking for two numbers and operation from users
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    choice = input("Which operation would you like to perform? (+, -, *, /): ")

    #if statements will do calculation based on which operator user chose
    #calling appropriate function for calculation and print out the result
    if choice == "+":
        result = add(a, b)
        print("The sum of {} and {} is {}".format(a, b, result))

    elif choice == "-":
        result = sub(a, b)
        print("The difference of {} and {} is {}".format(a, b, result))

    elif choice == "*":
        result = mul(a, b)
        print("The multiplication of {} and {} is {}".format(a, b, result))

    elif choice == "/":
        result = div(a, b)
        print("The quotient of {} and {} is {}".format(a, b, result))

    else:
        print("Invalid input. Please try again.")
        return

#Runiing the main function; calculator()
calculator()