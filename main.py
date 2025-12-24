import sys

tasks = []

def add_task(title):
    # Implementation by Ali Hashir
    tasks.append(title)
    print(f"Task '{title}' added successfully.")

def show_tasks():
    # Implementation by Momal Rana
    if not tasks:
        print("No tasks available.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index}: {task}")

def delete_task(index):
    # Implementation by Ashel Aftaab
    try:
        index = int(index)
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    # Simple menu CLI
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_task("Sample Task") # Placeholder
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task(0) # Placeholder
        elif choice == '4':
            break

if __name__ == "__main__":
    main()