
tasks = ["Buy milk", "Call num", "Finish python learning"]

print("My To-Do-List")

print("------------")

for index, value in enumerate(tasks, start = 1):
    print(f"{index}. {value}")


print("-----------")
print(f"Total number of tasks: {len(tasks)}")


    
