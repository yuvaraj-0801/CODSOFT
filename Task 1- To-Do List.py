import emoji


def add_task(l):
    n = int(input("Enter the No. of Tasks to be added : "))
    for i in range(n):
        name = input("Enter the Task : ")
        l.append(name)


def view_task(l):
    if len(l) > 0:
        print("The tasks are : ")
        for i in l:
            print(i)
    else:
        print("Error !!! Please add the task")


def update_task(l):
    n = input("Enter the task to be updated : ")
    n1 = input("Enter the new task : ")
    i = l.index(n)
    if n in l:
        l[i] = n1
    else:
        print("Task not found..")


def delete_task(l):
    n = input("Enter the task to be deleted : ")
    if n in l:
        l.remove(n)
    else:
        print("Task not found...")


def main():
    l = []
    while True:
        print()
        print("******** TO-DO List ********")
        print("1.Add")
        print("2.View")
        print("3.Update")
        print("4.Delete")
        print("5.Exit")

        ch = int(input("Enter your choice : "))
        print()

        if ch == 1:
            add_task(l)
            print("Task Added")
        elif ch == 2:
            view_task(l)
        elif ch == 3:
            update_task(l)
            print("Task updated")
        elif ch == 4:
            delete_task(l)
            print("Task deleted")
        elif ch == 5:
            print("Thank you :) ")
            print(emoji.emojize(":smiling_face:"))
            break
        else:
            print("invalid")


main()
