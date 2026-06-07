import json

class MemoryAgent:

    def __init__(self):
        print("Memory Agent Initialized")

    def remember(self, key, value):
        with open("memory.json", "r") as file:
            data = json.load(file)

        data[key] = value
 
        with open("memory.json", "w") as file:
            json.dump(data, file)

        print(f"Remembering: {key} = {value}")

    def recall(self, key):
        with open("memory.json", "r") as file:
            data = json.load(file)
            if key in data:
                print(data[key])
            else:
                print("Memory not found")
    
    def forget(self, key):
        with open("memory.json", "r") as file:
            data = json.load(file)
            if key in data:
                print(data[key])
        pass