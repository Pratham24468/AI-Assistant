import json

class NotesAgent:
    
    def __init__(self):
        print("Notes Agent Initialized")

    def add_note(self, title, content):
        with open("notes.json", "r") as file:
            data = json.load(file)
        next_id = max((item["id"] for item in data), default=0) + 1
        new_note = {
            "id": next_id,
            "title": title,
            "content": content
        }
        data.append(new_note)
        with open("notes.json", "w") as file:
            json.dump(data, file, indent=4)

    def view_notes(self):
        with open("notes.json", "r") as file:
            data = json.load(file)
        for note in data:
            print(note["id"])
            print(note["title"])
            print(note["content"])
        
    def delete_note(self, note_id):
        with open("notes.json", "r") as file:
            data = json.load(file)
        found = False
        for note in data:
            if note["id"] == note_id:
                found = True
                data.remove(note)
                break
        if not found:
            print("Note not Found")
        with open("notes.json", "w") as file:
            json.dump(data, file, indent=4)

    def search_notes(self, keyword):
        with open("notes.json", "r") as file:
            data = json.load(file)
        found = False
        keyword_lower = keyword.lower()
        for note in data:
            if keyword_lower in note["title"].lower() or keyword_lower in note["content"].lower():
                print(note["title"])
                print(note["content"])
                found = True
        if not found:
            print("No Matching notes")
    
    def count_notes(self):
        with open("notes.json", "r") as file:
            data = json.load(file)
        print(len(data))
        found = False
    def edit_note(self, id, new_title, new_content):
        with open("notes.json", "r") as file:
            data = json.load(file)
        found = False
        for note in data:
            if id == note["id"]:
                note["title"] = new_title
                note["content"] = new_content
                found = True
        if not found:
            print("Note not found")
        with open("notes.json", "w") as file:
            json.dump(data, file, indent=4)