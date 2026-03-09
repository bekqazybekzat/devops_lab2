from task_manager import TaskManager
from file_manager import FileManager

manager = TaskManager()
file_manager = FileManager()

manager.tasks = file_manager.load("tasks.json")

def menu():
    print("Task Manager")
    print("1 Add Task")
    print("2 List Tasks")
    print("3 Complete Task")
    print("4 Delete Task")
    print("5 Save Tasks")
    print("6 Exit")

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        desc = input("Description: ")
        manager.add_task(title, desc)

    elif choice == "2":
        manager.list_tasks()

    elif choice == "3":
        try:
            task_id = int(input("Task ID: "))
            if not manager.complete_task(task_id):
                print("Task not found")
        except:
            print("Invalid input")

    elif choice == "4":
        try:
            task_id = int(input("Task ID: "))
            if not manager.delete_task(task_id):
                print("Task not found")
        except:
            print("Invalid input")

    elif choice == "5":
        file_manager.save(manager.tasks, "tasks.json")

    elif choice == "6":
        file_manager.save(manager.tasks, "tasks.json")
        break

    else:
        print("Invalid option")





