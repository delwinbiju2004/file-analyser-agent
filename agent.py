import os
import anthropic
from dotenv import load_dotenv
from tools.read_file import read_file
from tools.calculate_stats import calculate_statistics
from tools.search_keywords import search_keywords
from tools.summarise_text import summarise_text

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

tools = [
    {
        "name": "read_file",
        "description": "Reads the content of a .txt or .csv file and returns it as text.",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Path to the file"}
            },
            "required": ["file_path"]
        }
    },
    {
        "name": "calculate_statistics",
        "description": "Calculates basic statistics (mean, min, max etc) from a CSV file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Path to the CSV file"}
            },
            "required": ["file_path"]
        }
    },
    {
        "name": "search_keywords",
        "description": "Searches for a keyword inside a file and returns matching lines.",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Path to the file"},
                "keyword": {"type": "string", "description": "Keyword to search for"}
            },
            "required": ["file_path", "keyword"]
        }
    },
    {
        "name": "summarise_text",
        "description": "Summarises the content of a text file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "Text content to summarise"}
            },
            "required": ["content"]
        }
    }
]

def run_tool(tool_name, tool_input):
    if tool_name == "read_file":
        return read_file(tool_input["file_path"])
    elif tool_name == "calculate_statistics":
        return calculate_statistics(tool_input["file_path"])
    elif tool_name == "search_keywords":
        return search_keywords(tool_input["file_path"], tool_input["keyword"])
    elif tool_name == "summarise_text":
        return summarise_text(tool_input["content"])
    else:
        return "Unknown tool."

def run_agent(file_path, question):
    print(f"\nQuestion: {question}")
    print(f"File: {file_path}\n")

    messages = [
        {"role": "user", "content": f"The file is located at: {file_path}\n\nQuestion: {question}"}
    ]

    while True:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    print("Answer:", block.text)
            break

        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"Using tool: {block.name}")
                    result = run_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            messages.append({"role": "user", "content": tool_results})

if __name__ == "__main__":
    file_path = input("Enter file path: ")
    question = input("Enter your question: ")
    run_agent(file_path, question)