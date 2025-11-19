# TO_DO LIST



This is a simple, command-line to-do list application written in Python. It allows you to add, view, and remove tasks directly from your terminal. It's a classic beginner project for learning Python fundamentals like lists, functions, loops, and user input.





#### Features



View Tasks: Displays all current tasks in a clean, numbered list.



Add Tasks: Allows you to add new tasks to your list. Empty or whitespace-only tasks are prevented.



Remove Tasks: Allows you to remove a task by its number.



User-Friendly Menu: A clear and simple menu that loops until the user decides to exit.



Error Handling: Safely handles invalid inputs, such as non-numeric choices for the menu or task removal.





#### Requirements



Python 3.x



(No external libraries are needed, as it only uses the built-in time module.)





#### How to Run



Make sure you have Python 3 installed on your system.



Save the code in a file named todo_list.py.



Open your terminal or command prompt.



Navigate (using cd) to the directory where you saved the file.



Run the application with the following command:



python todo_list.py





#### Example Usage ####



Here is what you'll see when you run the application:



Welcome to your To-Do List!



==============================

       TO-DO LIST MENU

==============================

1\. View tasks

2\. Add a task

3\. Remove a task

4\. Exit

------------------------------

Enter your choice (1-4): 2

Enter the task you want to add: Buy groceries



Successfully added: 'Buy groceries'



==============================

      TO-DO LIST MENU

==============================

1\. View tasks

2\. Add a task

3\. Remove a task

4\. Exit

------------------------------

Enter your choice (1-4): 2

Enter the task you want to add: Finish Python project



Successfully added: 'Finish Python project'



==============================

      TO-DO LIST MENU

==============================

1\. View tasks

2\. Add a task

3\. Remove a task

4\. Exit

------------------------------

Enter your choice (1-4): 1



--- Your Tasks ---

1\. Buy groceries

2\. Finish Python project

------------------



==============================

       TO-DO LIST MENU

==============================

1\. View tasks

2\. Add a task

3\. Remove a task

4\. Exit

------------------------------

Enter your choice (1-4): 3



--- Your Tasks ---

1\. Buy groceries

2\. Finish Python project

------------------

Enter the number of the task to remove: 1



Successfully removed: 'Buy groceries'



==============================

       TO-DO LIST MENU

==============================

1\. View tasks

2\. Add a task

3\. Remove a task

4\. Exit

------------------------------

Enter your choice (1-4): 4

Goodbye! Have a productive day!



