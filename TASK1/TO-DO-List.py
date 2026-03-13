# To-Do List Application with Task Status

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Show all tasks")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{idx}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter the task title: ")
    tasks.append({'title': title, 'completed': False})
    print(f"Task '{title}' added.")

def mark_completed(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['title']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed['title']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
