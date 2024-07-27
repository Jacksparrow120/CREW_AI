from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from pdf_reader_tool import read_pdf
from crewai_tools import tool, SerperDevTool
import os
from dotenv import load_dotenv
load_dotenv()


llm=Ollama(model = "openhermes")

report_reader = Agent(
    role = "Blood Report Reader",
    goal = 'Read and analyze given blood test report',
    backstory = 'You are skilled at reading, understanding and analyzing medical reports, creating summary of blood test reports in atleast 100 words.',
    tool = [read_pdf],
    Verbose = True,
    allow_delegation = False,
    llm = llm
)


searcher = Agent(
    role = 'Internet Search Specialist',
    goal = 'Use the Web Search tool to search for articles which can help to improve person health',
    backstory = 'You are an expert in finding articles from web which can help to improve person health if needed',
    tools=[SerperDevTool()],
    Verbose = True,
    allow_delegation = False,
    llm = llm
)


recommender = Agent(
    role = "Health Recommender",
    goal = 'you should give health recommendations and provide links to the relevant articles',
    backstory = 'You are skilled at recommending articles to the person based on their health report summary.',
    tool = [SerperDevTool()],
    Verbose = True,
    allow_delegation = False,
    llm = llm
)


task1 = Task(
    description = 'Analyze the blood sample reports',
    expected_output="Full analysis of blood sample report and give summary of reports",
    agent=report_reader
    )

task2 = Task(
    description = 'Search articles from the web related to the health issues on person',
    expected_output="provide with the relevant articles",
    agent=searcher
    )

task3 = Task(
    description = 'Recommend articles from the web related to the health issues for person',
    expected_output="Give the links to the articles which can help person to live good life",
    agent=recommender
    )

crew = Crew(
    agents=[report_reader, searcher,recommender],
    tasks=[task1,task2,task3],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff(inputs={'file_path': 'WM17S.pdf'})
