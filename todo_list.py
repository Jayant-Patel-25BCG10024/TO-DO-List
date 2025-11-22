#Console based to do list program

def show_menu():
    """Prints the main menu options to the console."""
    print("\n" + "=" * 30)
    print("      TO-DO LIST MENU")
    print("=" * 30)
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
    print("-" * 30)

def view_tasks(tasks):
    """Displays all current tasks, numbered."""
    print("\n--- Your Tasks ---")
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("------------------")

def add_task(tasks):
    """Prompts the user to add a new task and appends it to the list."""
    task = input("Enter the task you want to add: ")
    
    if task.strip():
        tasks.append(task.strip())
        print(f"\nSuccessfully added: '{task.strip()}'")
    else:
        print("\nCannot add an empty task.")

def remove_task(tasks):
    """Shows the task list and removes a task by its number."""
    
    view_tasks(tasks)
    
    if not tasks:
        return

    try:
        task_number_str = input("Enter the number of the task to remove: ")
        task_number = int(task_number_str)


        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"\nSuccessfully removed: '{removed_task}'")
        else:
            print(f"\nInvalid task number. Please enter a number between 1 and {len(tasks)}.")
            
    except ValueError:
        print("\nInvalid input. Please enter a number.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def main():
    
    tasks = []
    
    print("Welcome to your To-Do List!")
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        
        elif choice == '2':
            add_task(tasks)
        
        elif choice == '3':
            remove_task(tasks)
            
        elif choice == '4':
            print("\nGoodbye! Have a productive day!")
            break 

main()



