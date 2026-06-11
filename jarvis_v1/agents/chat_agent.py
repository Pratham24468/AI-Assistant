from agents.memory_agent import MemoryAgent
from agents.task_agent import TaskAgent
from agents.notes_agent import NotesAgent
from agents.research_agent import ResearchAgent

class ChatAgent:
    
    def __init__(self):
        self.memory = MemoryAgent()
        self.task = TaskAgent()
        self.notes = NotesAgent()
        self.research = ResearchAgent()
        print("Chat Agent Initialized")

    def process_command(self, command):
        parts = command.split()
        if first_word == "remember":
            self.memory.remember(parts[1], " ".join(parts[2:]))
        elif first_word == "recall":
            self.memory.recall(parts[1])
        elif first_word == "forget":
            self.memory.forget(parts[1])
        elif first_word == "show_memories":
            self.memory.show_all_memories()
        elif first_word == "memory_count":
            self.memory.memory_count()
        elif first_word == "clear_memory":
            self.memory.clear_memory()
        elif first_word == "search_memory":
            self.memory.search_memory(" ".join(parts[1:]))
        elif first_word == "add_task":
            self.task.add_task(" ".join(parts[1:]))
        elif first_word == "view_tasks":
            self.task.view_tasks()
        elif first_word == "complete_task":
            self.task.complete_task(int(parts[1]))
        elif first_word == "delete_task":
            self.task.delete_task(int(parts[1]))
        elif first_word == "search_task":
            self.task.search_task(" ".join(parts[1:]))
        elif first_word == "count_tasks":
            self.task.count_tasks()
        elif first_word == "view_notes":
            self.notes.view_notes()
        elif first_word == "delete_note":
            self.notes.delete_note(int(parts[1]))
        elif first_word == "search_notes":
            self.notes.search_notes(" ".join(parts[1:]))
        elif first_word == "count_notes":
            self.notes.count_notes()
        elif first_word == "view_research":
            self.research.view_research()
        elif first_word == "search_research":
            self.research.search_research(" ".join(parts[1:]))
        elif first_word == "delete_research":
            self.research.delete_research(int(parts[1]))
        elif first_word == "count_research":
            self.research.count_research()
