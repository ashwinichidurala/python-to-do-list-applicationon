import json
from datetime import datetime

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        try:
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def add_task(self, task, priority, due_date):
        self.tasks.append({
            "task": task,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        })
        self.save_tasks()

    def remove_task(self, task_index):
        del self.tasks[task_index]
        self.save_tasks()

    def complete_task(self, task_index):
        self.tasks[task_index]["completed"] = True
        self.save_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f)

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task['task']}, Priority: {task['priority']}, Due date: {task['due_date']}, Completed: {task['completed']}")

todo_list = TodoList()
while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task as completed")
    print("4. View tasks")
    print("5. Exit")
    option = input("Select an option: ")
    if option == "1":
        task = input("Enter a task: ")
        priority = input("Enter priority (high, medium, low): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        todo_list.add_task(task, priority, due_date)
    elif option == "2":
        task_index = int(input("Enter the task number to remove: ")) - 1
        todo_list.remove_task(task_index)
    elif option == "3":
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        todo_list.complete_task(task_index)
    elif option == "4":
        todo_list.view_tasks()
    elif option == "5":
        break
