def summarise_text(content: str) -> str:
    """Returns a shortened preview of long text content."""
    try:
        lines = content.strip().split("\n")
        total_lines = len(lines)
        total_words = len(content.split())
        preview = "\n".join(lines[:10])
        
        return (
            f"File Summary:\n"
            f"- Total lines: {total_lines}\n"
            f"- Total words: {total_words}\n\n"
            f"First 10 lines preview:\n{preview}"
        )
    except Exception as e:
        return f"Error summarising text: {str(e)}"