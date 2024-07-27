# CrewAI Blood Test Report Analyzer

This repository contains a project that uses the CrewAI framework to set up a team of agents for analyzing blood test reports, searching for relevant health articles, and providing health recommendations. The project leverages the `langchain_community.llms` for natural language processing tasks and uses tools like `PyPDF2` for reading PDF files.

## Project Structure

- **main.py**: The main script that sets up the agents, tasks, and the crew to perform the analysis, search, and recommendation tasks.
- **pdf_reader_tool.py**: A custom tool for reading and extracting text from PDF files.
- **.env**: Environment file containing the necessary environment variables.
- **sample.pdf**: A sample blood test report for testing the functionality.

## Requirements

- Python 3.7+
- CrewAI
- langchain_community.llms
- PyPDF2
- dotenv

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crewai-blood-test-analyzer.git
   cd crewai-blood-test-analyzer
