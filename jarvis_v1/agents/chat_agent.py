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
        first_word = parts[0]
        if first_word == "remember":
            self.memory.remember(parts[1], parts[2])
        
