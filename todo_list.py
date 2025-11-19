import time

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
        # enumerate adds a counter to an iterable
        # We use start=1 to begin numbering from 1 instead of 0
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("------------------")

def add_task(tasks):
    """Prompts the user to add a new task and appends it to the list."""
    task = input("Enter the task you want to add: ")
    
    # .strip() removes any leading/trailing whitespace
    if task.strip():
        tasks.append(task.strip())
        print(f"\nSuccessfully added: '{task.strip()}'")
    else:
        print("\nCannot add an empty task.")

def remove_task(tasks):
    """Shows the task list and removes a task by its number."""
    
    # First, show the user what tasks they have
    view_tasks(tasks)
    
    if not tasks:
        # If the list is empty, we can't remove anything
        return

    try:
        # Get user input for the task number to remove
        task_number_str = input("Enter the number of the task to remove: ")
        
        # Convert the input string to an integer
        task_number = int(task_number_str)

        # Check if the number is within the valid range of the list
        # List indices are 0-based, so we check from 1 to len(tasks)
        if 1 <= task_number <= len(tasks):
            # We subtract 1 to get the correct 0-based index for .pop()
            removed_task = tasks.pop(task_number - 1)
            print(f"\nSuccessfully removed: '{removed_task}'")
        else:
            print(f"\nInvalid task number. Please enter a number between 1 and {len(tasks)}.")
            
    except ValueError:
        # This except block runs if int() fails (e.g., user typed "abc")
        print("\nInvalid input. Please enter a number.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"\nAn error occurred: {e}")

def main():
    """Main function to run the to-do list application."""
    
    # This list will hold all our task strings
    tasks = []
    
    print("Welcome to your To-Do List!")

    # The main application loop
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
            break  # Exit the while loop, ending the program

#To run the program
main()

