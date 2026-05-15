def search_keywords(file_path: str, keyword: str) -> str:
    """Searches for a keyword in a file and returns matching lines."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        matches = []
        for i, line in enumerate(lines, 1):
            if keyword.lower() in line.lower():
                matches.append(f"Line {i}: {line.strip()}")
        
        if matches:
            return f"Found {len(matches)} match(es) for '{keyword}':\n\n" + "\n".join(matches)
        else:
            return f"No matches found for '{keyword}'."
    
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"Error searching file: {str(e)}"