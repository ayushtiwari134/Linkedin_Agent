from crewai import Crew, Process
from tasks import find_data, post_writing, humanizing_task
from agents import data_researcher, linkedin_post_writer, humanizer_agent

crew = Crew(
    agents= [data_researcher, linkedin_post_writer, humanizer_agent],
    tasks= [find_data, post_writing, humanizing_task],
    process= Process.sequential,
    verbose= 3
)

result = crew.kickoff(inputs = {"project": "LinkedIn post creation using CrewAI agents"})
print(result)
