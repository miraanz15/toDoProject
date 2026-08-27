tasks = ["Buy milk", "Call num", "Finish python lesson"]

def show_tasks():
    print("TODO-LIST")
    print("----------")
    for index,task in enumerate(tasks, start=1):
        print(f"{index}, {task}")
    print("----------")
    print(f"You have {len(tasks)} tasks \n")

def add_task(task):
    tasks.append(task)

def remove_task(task):
    tasks.remove(task)    

def count_tasks():
    return len(tasks)


show_tasks()

add_task("Water plants")
show_tasks()

remove_task("Call num")
show_tasks()

total = count_tasks()
print(f"Total tasks: {total}")