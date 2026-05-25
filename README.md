# File Analyser Agent

An AI-powered command-line tool that reads text and CSV files and answers questions about them in plain English. It uses the Anthropic Claude API to understand questions and select the right tool for the job.

## What It Does

You give the program a file and a question, and it returns a clear answer. For example:
- "What is the average score in this file?"
- "Find all lines that mention the word error"
- "Summarise this document"

## Features

- Reads `.txt` and `.csv` files
- Calculates statistics (average, minimum, maximum) on CSV data
- Searches files for keywords
- Summarises text files (line count, word count, preview)
- Clear error messages instead of crashes

## Requirements

- Python 3.10 or higher
- An Anthropic API key

## Installation

1. Clone the repository:
git clone https://github.com/delwinbiju2004/file-analyser-agent.git
cd file-analyser-agent

2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install the dependencies:
pip install -r requirements.txt
4. Create a `.env` file in the project folder and add your API key:
ANTHROPIC_API_KEY=your-api-key-here

## How to Use

Run the program from the terminal:
python3 agent.py

The program will ask for:
1. A file path (for example, `sample.csv`)
2. A question about the file

It will then process the file and print the answer.

## Running Tests

To run the test suite:

pytest tests/ -v
## Project Structure
file-analyser-agent/
├── agent.py              Main program and AI agent logic
├── config/
│   └── env_loader.py     Loads the API key from .env
├── tools/
│   ├── read_file.py      Reads .txt and .csv files
│   ├── calculate_stats.py Calculates CSV statistics
│   ├── search_keywords.py Searches files for keywords
│   └── summarise_text.py  Summarises text files
├── tests/
│   └── test_tools.py     Test suite for all tools
├── requirements.txt      List of dependencies
└── .env                  API key (not shared on GitHub)
## Notes

The program only reads files. It never edits or deletes them. The API key is kept in a `.env` file which is excluded from version control for security.