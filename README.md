# JARVIS V1

A modular offline AI assistant built in Python.

## Vision

JARVIS V1 is the foundation for a future multi-agent AI system.

The goal is to create a centralized brain capable of managing multiple specialized agents such as memory, tasks, notes, research, and conversation.

This project focuses on architecture, modularity, and agent coordination before integrating large language models.

---

## Features

### Memory Agent
- Store memories
- Retrieve memories
- Search memories
- Delete memories

### Task Agent
- Create tasks
- View tasks
- Complete tasks
- Delete tasks

### Notes Agent
- Create notes
- View notes
- Delete notes

### Research Agent
- Search local knowledge
- Summarize stored information
- Assist other agents

### Chat Agent
- Handle conversations
- Act as the user interface layer
- Route requests to other agents

---

## Architecture

```text
User
 │
 ▼
Main Brain
 │
 ├── Memory Agent
 ├── Task Agent
 ├── Notes Agent
 ├── Research Agent
 └── Chat Agent
```

---

## Project Structure

```text
jarvis_v1/

main.py

agents/
│
├── __init__.py
├── chat_agent.py
├── memory_agent.py
├── task_agent.py
├── notes_agent.py
└── research_agent.py

data/
│
├── memory.json
├── tasks.json
└── notes.json
```

---

## Design Principles

- Modular architecture
- Agent-based design
- Local-first storage
- Human-readable data
- Expandable system
- Future AI integration

---

## Future Roadmap

### V1
- Modular agents
- JSON-based memory
- Task management
- Note management
- Local research system

### V2
- Ollama integration
- Local LLM support
- Semantic memory
- Better reasoning

### V3
- Multi-agent collaboration
- Tool calling
- Autonomous workflows

### V4
- Advanced reasoning engine
- Long-term memory
- Full personal assistant capabilities

---

## Tech Stack

- Python
- JSON
- OOP
- Modular Architecture

Future:
- FastAPI
- Ollama
- Vector Database
- RAG
- Local LLMs

---

## Goal

Build a clean, scalable foundation for future agentic AI systems while strengthening software engineering and Python development skills.