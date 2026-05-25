def count_lines(content: str) -> int:
    """Counts the number of lines in text content."""
    if not content.strip():
        return 0
    return len(content.strip().split("\n"))


def count_words(content: str) -> int:
    """Counts the number of words in text content."""
    return len(content.split())


def preview_lines(content: str, n: int = 10) -> str:
    """Returns a preview of the first N lines of text content."""
    lines = content.strip().split("\n")
    preview = "\n".join(lines[:n])
    return preview


def summarise_text(content: str) -> str:
    """Combines line count, word count, and preview into one summary."""
    try:
        total_lines = count_lines(content)
        total_words = count_words(content)
        preview = preview_lines(content, 10)

        return (
            f"File Summary:\n"
            f"- Total lines: {total_lines}\n"
            f"- Total words: {total_words}\n\n"
            f"First 10 lines preview:\n{preview}"
        )
    except Exception as e:
        return f"Error summarising text: {str(e)}"