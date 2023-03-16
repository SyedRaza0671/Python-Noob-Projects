user_input = ""

while user_input != "quit":
    num1 = float(input("Number : "))
    op = str(input("Operator : "))
    num2 = float(input("Number : "))

    if op == "+":
        print("Result : ", (num1 + num2))

    elif op == "-":
        print("Result : ", (num1 - num2))

    elif op == "/":
        print("Result : ", (num1 / num2))

    elif op == "*":
        print("Result : ", (num1 * num2))

    elif op == "%":
        print("Result : ", (num1 % num2))
    
    else:
        print("Invalid Operator!")
    
    user_input = input("Waiting for Command : ")
    if user_input == "quit" :
        break

