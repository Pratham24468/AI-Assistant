import json
import os

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
                print(data, data[key])
            else:
                print("Memory not found")
    
    def forget(self, key):
        with open("memory.json", "r") as file:
            data = json.load(file)
            if key in data:
                del data[key]
            else:
                print("Memory not found")
        with open("memory.json", "w") as file:
            json.dump(data, file, indent=4)

    def show_all_memories(self):
        with open("memory.json", "r") as file:
            data = json.load(file)
            for key in data:
                print(data[key])

    def memory_count(self):
        with open("memory.json", "r") as file:
            data = json.load(file)
            print(len(data))

    def clear_memory(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.abspath(
            os.path.join(current_dir, "..", "data", "memory.json")
        )

        with open(file_path, "w") as file:
            json.dump({}, file, indent=4)

    def search_memory(self, keyword):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.abspath(
            os.path.join(current_dir, "..", "data", "memory.json")
        )

        if not os.path.exists(file_path):
            return {}

        with open(file_path, "r") as file:
            try:
                memory_data = json.load(file)
            except json.JSONDecodeError:
                return {}

        results = {}
        keyword_lower = keyword.lower()

        for key, value in memory_data.items():
            if keyword_lower in key.lower() or keyword_lower in str(value).lower():
                results[key] = value

        return results
