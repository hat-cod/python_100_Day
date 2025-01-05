# Function to display the list of tasks
def show_tasks(tasks):
    if len(tasks) == 0:
        print("You have no tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")



# exemple 2

# List to store tasks
tasks = []

# Main loop to interact with the user
while True:
    print("\n--- Task List ---")
    action = input("Do you want to 'add' a task, 'view' tasks, or 'exit'? ").lower()

    if action == "add":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif action == "view":
        show_tasks(tasks)

    elif action == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please choose 'add', 'view', or 'exit'.")





# Explanation:
# Function:

# show_tasks(tasks): A function that shows all tasks in the list. If there are no tasks, it tells the user that there are no tasks to show.
# Lists:

# tasks: A list that stores all the tasks added by the user.
# Error Handling:

# Simple error handling is done for invalid input when the user is asked to choose an action (add, view, or exit). If the input doesn't match one of those options, the program will prompt the user to enter a valid command.
# Looping:

# The user can repeatedly add tasks, view tasks, or exit the program. The loop will keep running until the user chooses to exit.
# Example