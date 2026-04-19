import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return file.readlines()

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        file.writelines(tasks)

def add_task():
    task = input("Enter new task: ")
    tasks = load_tasks()
    tasks.append(task + " | Pending\n")
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")

def complete_task():
    view_tasks()
    tasks = load_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        if "Completed" in tasks[num - 1]:
            print("Task already completed.")
        else:
            tasks[num - 1] = tasks[num - 1].replace("Pending", "Completed")
            save_tasks(tasks)
            print("Task marked as completed!")
    except:
        print("Invalid input.")

def delete_task():
    view_tasks()
    tasks = load_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except:
        print("Invalid input.")

def menu():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete
