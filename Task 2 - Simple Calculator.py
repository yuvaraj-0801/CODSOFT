# Simple Calculator using Python

import emoji


while True:
    print("Select the operation : ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")
    print()
    ch = int(input("Enter your choice : "))
    print()
    if ch < 5:
        n1 = int(input("Enter the First value : "))
        n2 = int(input("Enter the Second value : "))
        print()
        if ch == 1:
            print("Addition Operation ")
            print(n1, "+", n2, "=", n1 + n2)
        elif ch == 2:
            print("Subtraction Operation ")
            print(n1, "-", n2, "=", n1 - n2)
        elif ch == 3:
            print("Division Operation ")
            print(n1, "/", n2, "=", n1 / n2)
        elif ch == 4:
            print("Multiplication Operation ")
            print(n1, "*", n2, "=", n1 * n2)
        print()
        o = input("Do you want to continue? (y/n) : ")
        if o == 'y':
            continue
        else:
            print()
            print("Thank you :) ")
            print(emoji.emojize(":smiling_face:"))
            break
    else:
        print("Error!!! Select the correct operation")
        print()
