def read_file(file_path: str) -> str:
    """Reads a .txt or .csv file and returns its content as a string."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"