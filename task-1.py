import json
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("No saved tasks found.")

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Complete" if task['complete'] else "Incomplete"
                print(f"{index}. [{status}] {task['title']} - {task['date']}")

    def add_task(self, title):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tasks.append({'title': title, 'date': date, 'complete': False})
        self.save_tasks()
        print(f'Task "{title}" added successfully.')

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f'Task "{deleted_task["title"]}" deleted successfully.')
        else:
            print("Invalid task index.")

    def edit_task(self, index, new_title):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]['title'] = new_title
            self.save_tasks()
            print(f'Task edited successfully.')
        else:
            print("Invalid task index.")

    def toggle_task_completion(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]['complete'] = not self.tasks[index - 1]['complete']
            self.save_tasks()
            print("Task completion status toggled successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List:")
        todo_list.display_tasks()

        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Mark Task As Completed")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            title = input("Enter your task: ")
            todo_list.add_task(title)
        elif choice == '2':
            index = int(input("Enter the task to delete: "))
            todo_list.delete_task(index)
        elif choice == '3':
            index = int(input("Enter the task to edit: "))
            new_title = input("Enter your new task: ")
            todo_list.edit_task(index, new_title)
        elif choice == '4':
            index = int(input("Enter the task to toggle completion: "))
            todo_list.toggle_task_completion(index)
        elif choice == '5':
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
