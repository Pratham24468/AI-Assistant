import json

class ResearchAgent:
    def __init__(self):
        print("Research Agent Initialized")
        pass

    def add_research(self, topic, findings):
        with open("research.json", "r") as file:
            data = json.load(file)
        next_id = max((item["id"] for item in data), default=0) + 1
        new_research = {
            "id": next_id,
            "topic": topic,
            "findings": findings
        }
        data.append(new_research)
        with open("research.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Research Saved Successfully! Topic: {topic}")

    def view_research(self):
        with open("research.json", "r") as file:
            data = json.load(file)
        for research in data:
            print(research["id"])
            print(research["topic"])
            print(research["findings"])

    def search_research(self, keyword):
        with open("research.json", "r") as file:
            data = json.load(file)
        found = False
        keyword_lower = keyword.lower()
        for research in data:
            if keyword_lower in research["topic"].lower() or keyword_lower in research["findings"].lower():
                print(research["id"])
                print(research["topic"])
                print(research["findings"])
                found = True
        if not found:
            print("No Matching Research")

    def delete_research(self, research_id):
        with open("research.json", "r") as file:
            data = json.load(file)
        found = False
        for research in data:
            if research["id"] == research_id:
                found = True
                data.remove(research)
                break
        if not found:
            print("Research not Found")
        with open("research.json", "w") as file:
            json.dump(data, file, indent=4)
        

    def count_research(self):
        with open("research.json", "r") as file:
            data = json.load(file)
        print(len(data))