from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv


def get_llm():
    api_key = os.getenv("OPENROUTER_API_KEY")
    return LLM(
        model="openrouter/deepseek/deepseek-r1",
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

llm = get_llm()


load_dotenv()  
serper_api_key = os.getenv("SERPER_API_KEY")



class Section(BaseModel):
    title: str
    high_level_goal: str
    why_important: str
    sources: List[str]
    content_outline: List[str]

class EducationalPlan(BaseModel):
    sections: List[Section]
@CrewBase
class EduResearch():
    """EduResearch crew"""

    # Updated YAML configuration files for agents and tasks
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        """Defines the researcher agent"""
        return Agent(
            config=self.agents_config['researcher'],  # Uses the researcher configuration
            verbose=True,
            tools = [SerperDevTool()],
            llm=llm,  
        )

    @agent
    def planner(self) -> Agent:
        """Defines the planner agent"""
        return Agent(
            config=self.agents_config['planner'],  # Uses the planner configuration
            verbose=True,
            llm=llm,
        )

    @task
    def research_task(self) -> Task:
        """Defines the research task"""
        return Task(
            config=self.tasks_config['research_task'],  # Uses the research_task configuration
        )

    @task
    def planning_task(self) -> Task:
        """Defines the planning task"""
        return Task(
            config=self.tasks_config['planning_task'],  # Uses the planning_task configuration
            output_pydantic=EducationalPlan
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EduResearch crew"""
        return Crew(
            agents=self.agents,  # Automatically created by @agent decorators
            tasks=self.tasks,  # Automatically created by @task decorators
            process=Process.sequential,  # Sequential process for task execution
            verbose=True,
        )
