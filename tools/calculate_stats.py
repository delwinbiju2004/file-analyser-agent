import pandas as pd

def calculate_statistics(file_path: str) -> str:
    """Reads a CSV file and returns basic statistics."""
    try:
        df = pd.read_csv(file_path)
        stats = df.describe().to_string()
        return f"Statistics for '{file_path}':\n\n{stats}"
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"Error calculating statistics: {str(e)}"