# A simple CLI To-Do List application in Python

# The list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Added task: '{task}'")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")

# Function to delete a task
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed task: '{removed_task}'")
    else:
        print("Invalid task number.")

# Main function to run the app
def run_app():
    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter a task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    run_app()
