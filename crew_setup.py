
import json
from crewai import Agent
import os

def load_agents():
    base_path = os.path.join(os.path.dirname(__file__), "agents")
    agents = []
    for file in os.listdir(base_path):
        if file.endswith(".json"):
            with open(os.path.join(base_path, file), "r") as f:
                config = json.load(f)
                agents.append(Agent(
                    role=config["role"],
                    goal=config["goal"],
                    backstory=config["backstory"],
                    verbose=True
                ))
    return agents
