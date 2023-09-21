def add(num1, num2):
    return(num1 + num2)

def sub(num1, num2):
    return(num1 - num2)

def mul(num1, num2):
    return(num1 * num2)

def div(num1, num2):
    return(num1 / num2)

def mod(num1, num2):
    return(num1 % num2)

print("**********WELCOME TO PYTHON CALCULATOR**********\n")

while(1):
    num1 = int(input("\nEnter first number:  "))
    num2 = int(input("Enter second number:  "))

    print("\nChoose any one option from below options:  ")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulous\n")

    choice = int(input("Enter your choice:  "))

    if(choice == 1):
        print("Answer = ",add(num1, num2))
    elif(choice == 2):
        print("Answer = ",sub(num1, num2))
    elif(choice == 3):
        print("Answer = ",mul(num1, num2))
    elif(choice == 4):
        print("Answer = ",div(num1, num2))
    elif(choice == 5):
        print("Answer = ",mod(num1, num2))
    else:
        print("Invalid input...")
        

    print("Do you want to continue(Y/N)?")
    con = input()
    if(con == "N"):
        break

    






