tasks = [
    {"text": "Buy milk", "done": False},
    {"text": "Call mum", "done": False},
    {"text": "Finish Python lesson", "done": False},
]


def show_tasks():
    print("\nTO-DO LIST")
    print("-----------")
    if not tasks:
        print("No tasks to show.")
        print("-----------")
        return
    for index, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{index}. [{mark}] {task['text']}")
    print("-----------")
    print(f"You have {len(tasks)} tasks.")


def add_task(text):
    for task in tasks:
        if task["text"] == text:
            print(f"Task '{text}' is already in the list.")
            return
    tasks.append({"text": text, "done": False})
    print(f"Added: {text}")


def remove_task_at(pos):
    index = pos - 1
    if index < 0 or index >= len(tasks):
        print("Invalid position.")
        return
    removed = tasks.pop(index)
    print(f"Removed: {removed['text']}")


def mark_done(pos):
    index = pos - 1
    if index < 0 or index >= len(tasks):
        print("Invalid position.")
        return
    tasks[index]["done"] = True
    print(f"Marked done: {tasks[index]['text']}")


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task by position")
    print("4. Mark task as done")


while True:
    show_menu()
    choice = input("\nEnter your choice or 'q' to quit: ").strip()

    if choice == "q":
        print("Goodbye!")
        break

    elif choice == "1":
        show_tasks()

    elif choice == "2":
        text = input("Enter the task: ").strip()
        if text:
            add_task(text)
        else:
            print("A task cannot be empty.")

    elif choice == "3":
        show_tasks()
        pos = input("Which position? ").strip()
        if not pos.isdigit():
            print("Please type a number.")
            continue
        remove_task_at(int(pos))

    elif choice == "4":
        show_tasks()
        pos = input("Which position? ").strip()
        if not pos.isdigit():
            print("Please type a number.")
            continue
        mark_done(int(pos))

    else:
        print("Invalid choice. Please choose from the menu.")
