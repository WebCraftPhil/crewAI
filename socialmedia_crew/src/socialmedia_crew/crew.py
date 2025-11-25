from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class SocialmediaCrew():
    """SocialmediaCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def social_media_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'], # type: ignore[index]
            verbose=True
        )

    @agent
    def content_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['content_editor'], # type: ignore[index]
            verbose=True
        )

    @agent
    def content_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_optimizer'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def instagram_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['instagram_research_task'], # type: ignore[index]
        )

    @task
    def content_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_creation_task'], # type: ignore[index]
        )

    @task
    def content_editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_editing_task'], # type: ignore[index]
        )

    @task
    def content_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_optimization_task'], # type: ignore[index]
            output_file='instagram_content.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SocialmediaCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
