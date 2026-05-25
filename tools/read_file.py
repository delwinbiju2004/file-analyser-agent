import os
import csv

def read_file(file_path: str) -> str:
    """Reads a .txt or .csv file. Validates existence and format before reading."""
    if not os.path.exists(file_path):
        return f"Error: The file '{file_path}' was not found."

    if not (file_path.endswith(".txt") or file_path.endswith(".csv")):
        return "Error: Only .txt and .csv files are supported."

    try:
        if file_path.endswith(".csv"):
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)

            if not rows:
                return "The CSV file is empty."

            headers = list(rows[0].keys())
            output = ", ".join(headers) + "\n"
            for row in rows:
                output += ", ".join(str(row[h]) for h in headers) + "\n"
            return output
        else:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"