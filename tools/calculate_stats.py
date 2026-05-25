import pandas as pd

def calculate_average(df, column_name):
    if column_name not in df.columns:
        return f"Error: Column '{column_name}' not found."
    try:
        numeric_col = pd.to_numeric(df[column_name], errors='coerce')
        if numeric_col.isna().all():
            return f"Error: Column '{column_name}' has no numeric data."
        return round(numeric_col.mean(), 2)
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_minimum(df, column_name):
    if column_name not in df.columns:
        return f"Error: Column '{column_name}' not found."
    try:
        numeric_col = pd.to_numeric(df[column_name], errors='coerce')
        if numeric_col.isna().all():
            return f"Error: Column '{column_name}' has no numeric data."
        return numeric_col.min()
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_maximum(df, column_name):
    if column_name not in df.columns:
        return f"Error: Column '{column_name}' not found."
    try:
        numeric_col = pd.to_numeric(df[column_name], errors='coerce')
        if numeric_col.isna().all():
            return f"Error: Column '{column_name}' has no numeric data."
        return numeric_col.max()
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_statistics(file_path: str) -> str:
    try:
        df = pd.read_csv(file_path)
        numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

        if not numeric_columns:
            return "No numeric columns found in the CSV file."

        result = f"Statistics for '{file_path}':\n\n"
        for col in numeric_columns:
            avg = calculate_average(df, col)
            min_val = calculate_minimum(df, col)
            max_val = calculate_maximum(df, col)
            result += f"Column: {col}\n"
            result += f"  Average: {avg}\n"
            result += f"  Minimum: {min_val}\n"
            result += f"  Maximum: {max_val}\n\n"

        return result

    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"Error calculating statistics: {str(e)}"