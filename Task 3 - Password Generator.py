import random
import string
import emoji


def password_generator(length):
    char = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    pwd = char + digits + symbols
    password = ""
    for i in range(length):
        password += ''.join(random.choice(pwd))
    return password


def main():
    print()
    print("******** Password Generator ********")
    while True:
        print()
        n = int(input("Enter the Length of the password : "))
        if n < 0:
            print("Error !!! Enter a positive number")
            continue
        else:
            new_password = password_generator(n)
            print()
            print("Password : ", new_password)
        print()
        ch = input("Do you want to generate new password ? (y/n) : ")
        if ch == 'y':
            continue
        else:
            print("Thank You :)")
            print(emoji.emojize(":smiling_face:"))
            break


main()


