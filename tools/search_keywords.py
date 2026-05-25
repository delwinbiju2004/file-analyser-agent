import csv


def search_in_text(file_path: str, keyword: str) -> list:
    """Searches for a keyword in a text file line by line."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    matches = []
    for i, line in enumerate(lines, 1):
        if keyword.lower() in line.lower():
            matches.append(f"Line {i}: {line.strip()}")

    return matches


def search_in_csv(file_path: str, keyword: str, column_name: str = None) -> list:
    """Searches for a keyword across rows or in a specific column of a CSV file."""
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    matches = []
    for i, row in enumerate(rows, 1):
        if column_name:
            if column_name in row and keyword.lower() in str(row[column_name]).lower():
                matches.append(f"Row {i}: {row}")
        else:
            for value in row.values():
                if keyword.lower() in str(value).lower():
                    matches.append(f"Row {i}: {row}")
                    break

    return matches


def search_keywords(file_path: str, keyword: str) -> str:
    """Main function: searches for a keyword in .txt or .csv files."""
    try:
        if file_path.endswith(".csv"):
            matches = search_in_csv(file_path, keyword)
            label = "matching row(s)"
        else:
            matches = search_in_text(file_path, keyword)
            label = "match(es)"

        if matches:
            return f"Found {len(matches)} {label} for '{keyword}':\n\n" + "\n".join(matches)
        else:
            return f"No matches found for '{keyword}'."

    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"Error searching file: {str(e)}"