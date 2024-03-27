# Project: To-Do List Application

def add_task(tasks,task):
    tasks.append(task)
    print("Task has been added!")

def view_task(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("To-Do Lists:")
        for task in range(len(tasks)):
            print(f"{task + 1}. {tasks[task]}")

def delete_task(tasks):
    try:
        task = int(input("Which task would you like to delete: ")) - 1
        if 0 <= task < len(tasks):
            deleted_task = tasks.pop(task)
            print(f"Task {task} has been deleted!")
        else:
            print("Sorry seems as this is an invalid task number")
    except ValueError:
        print("Seems you have provided an invalid input, please enter a valid number.")

def menu():
    print("Main Menu:")
    print("1. Add a task")
    print("2. View task(s)")
    print("3. Delete a task")
    print("4. Quit")

def to_do():
    tasks = []
    print("Welcome to the To-Do List App!")
    print("\n")
    while True:
        print("\n")
        menu()
        option = input("What would you like to do? ")
        try:
            if option == "1":
                task = input("What task would you like to add: ")
                add_task(tasks, task)
            elif option == "2":
                view_task(tasks)
            elif option == "3":
                if not tasks:
                    print("Seems there are no tasks to be deleted")
                else:
                    delete_task(tasks)
            elif option == "4":
                print("Have a nice day! Thank you for using To-Do List App!")
                break
            else:
                print("Seems your choice is not on the menu, please try again.")
        except ValueError:
            print("Seems you have provided an invalid input, please enter a valid number.")

to_do()


