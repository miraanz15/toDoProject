tasks = ["Buy milk", "Call num", "Finish python lesson"]

def show_tasks():
    print("TO-DO-LIST")
    print("-----------")
    if not tasks:
        print("No tasks to show \n -------------")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print(f"You have {len(tasks)} tasks. \n -------------")

def add_task(task):
    if task in tasks:
        print(f"Task {task} already in the list")
        return
    tasks.append(task)
    print(f"Task {task} added to list \n")

def remove_task(task):
    if task not in tasks:
        print(f"Task {task} not found in list. Unable to remove.")
        return
    tasks.remove(task)
    print(f"Task {task} removed from list")

def pop_task_at_pos(pos):
    index = pos - 1
    if index < 0 or index >= len(tasks):
        print("Invalid position.")
        return
    removed = tasks.pop(index)
    print(f"Task {removed} removed from position {pos} \n")

def insert_task_at_pos(task, pos):
    index = pos - 1
    if index < 0 or index > len(tasks):
        print("Invalid position.")
        return
    tasks.insert(index, task)
    print(f"Task {task} added at position {pos} \n")

def show_menu():
    print("What would you like to do?")        
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Insert task at position")
    print("5. Pop task at specific position")

while True:
    show_menu()
    choice = input("\nPlease enter your choice or 'q' to quit:  ").strip()
    if choice == 'q':
        print("Goodbye!")
        break
    elif choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Please enter your task.").strip()
        add_task(task)
    elif choice == '3':
        task = input("Please enter the task to be removed.").strip()
        remove_task(task)
    elif choice == '4':
        task = input("Please enter the task to be added.").strip()
        pos = input("Please enter the position to add the task.").strip()
        if not pos.isdigit():
            print("Invalid position.")
            continue
        insert_task_at_pos(task, int(pos))
    elif choice == '5':
        pos = input("Enter the position to remove the task").strip()
        if not pos.isdigit():
            print("Invalid position")
            continue
        pop_task_at_pos(int(pos))
    else:
        print("Invalid choice. Please chose a valid option from the menu.")





            





        