class Task:
    def __init__(self, id, title, description, priority):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    # Implement other methods here...

def display_menu():
    print("Task Manager Menu")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Filter Tasks by Priority")
    print("6. Exit")

def main():
    task_manager = TaskManager()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("Selected: Add Task")
            # Call add_task() method
        elif choice == "2":
            print("Selected: Edit Task")
            # Call edit_task() method
        elif choice == "3":
            print("Selected: Delete Task")
            # Call delete_task() method
        elif choice == "4":
            print("Selected: View All Tasks")
            # Call view_all_tasks() method
        elif choice == "5":
            print("Selected: Filter Tasks by Priority")
            # Call filter_tasks_by_priority() method
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
