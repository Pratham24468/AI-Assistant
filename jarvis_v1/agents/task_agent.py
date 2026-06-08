import json

class TaskAgent:
    
    def __init__(self):
        print("Task Agent Initialized")
    
    def add_task(self, task_name):
        with open("task.json", "r") as file:
            data = json.load(file)
        next_id = max((item["id"] for item in data), default=0) + 1
        new_task = {
            "id": next_id,
            "task": task_name,
            "completed": False
        }
        data.append(new_task)
        with open("task.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Task Added: {task_name}")
    
    def view_tasks(self):
        with open("task.json", "r") as file:
            data = json.load(file)
        for task in data:
            print(task["id"])
            print(task["task"])
            print(task["completed"])
    
    def complete_task(self, task_id):
        with open("task.json", "r") as file:
            data = json.load(file)
        found = False
        for task in data:
            if task["id"] == task_id:
                found = True
                if task["completed"] == True:
                    print("Task already completed")
                elif task["completed"] == False:
                    task["completed"] = True
        if not found:
            print("Task not Found")
        with open("task.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def delete_task(self, task_id):
        with open("task.json", "r") as file:
            data = json.load(file)
        found = False
        for task in data:
            if task["id"] == task_id:
                found = True
                data.remove(task)
                break
        if not found:
            print("Task not Found")
        with open("task.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def search_task(self, keyword):
        with open("task.json", "r") as file:
            data = json.load(file)
        found = False
        keyword_lower = keyword.lower()
        for task in data:
            if keyword_lower in task["task"].lower():
                print(task["task"])
                found = True
        if not found:
            print("No Matching task")
    
    def count_tasks(self):
        with open("task.json", "r") as file:
            data = json.load(file)
        print(len(data))
        