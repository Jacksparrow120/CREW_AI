# Blood Report Analysis and Health Recommendation System

This project is designed to analyze blood test reports, search for relevant health articles on the web, and provide health recommendations based on the analysis. The system utilizes multiple AI agents working in tandem to achieve these tasks.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project leverages the CrewAI framework to create a team of AI agents that perform the following tasks:
1. **Read and analyze blood test reports**.
2. **Search for relevant health articles on the web**.
3. **Provide health recommendations based on the analysis**.

## Project Structure

project/

├── .env

├── main.py

├── pdf_reader_tool.py

├── requirements.txt

├── WM17S.pdf

└── README.md



- `.env`: Environment variables file containing API keys and other configurations.
- `main.py`: The main script that sets up and runs the CrewAI agents and tasks.
- `pdf_reader_tool.py`: Custom tool to read and extract text from PDF files.
- `requirements.txt`: List of Python dependencies.
- `WM17S.pdf`: Sample blood test report PDF.
- `README.md`: This readme file.

## Requirements

- Python 3.8 or higher
- CrewAI framework
- PyPDF2 library
- dotenv library

## Setup

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the environment variables**:
    Create a `.env` file in the project root directory and add your API keys:
    ```dotenv
    SERPER_API_KEY=your_serper_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Place your PDF report**:
    Ensure you have your blood test report in the root directory. The provided sample report is `WM17S.pdf`.

## Running the Project

To run the project, simply execute the `main.py` script:
```bash
python main.py
