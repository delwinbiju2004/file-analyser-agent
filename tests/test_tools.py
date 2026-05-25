import os
import sys

# Allow importing from the parent folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.read_file import read_file
from tools.calculate_stats import calculate_statistics
from tools.search_keywords import search_keywords
from tools.summarise_text import count_lines, count_words, preview_lines


# ---------- Test fixtures (sample files created for testing) ----------

def setup_module(module):
    """Creates sample test files before tests run."""
    with open("test_sample.txt", "w") as f:
        f.write("hello world\nthis is a test\nerror found here\nlast line")

    with open("test_sample.csv", "w") as f:
        f.write("Name,Score\nAlice,80\nBob,90\nCharlie,100")


def teardown_module(module):
    """Deletes sample test files after tests finish."""
    for file in ["test_sample.txt", "test_sample.csv"]:
        if os.path.exists(file):
            os.remove(file)


# ---------- read_file tests ----------

def test_read_txt_file():
    result = read_file("test_sample.txt")
    assert "hello world" in result

def test_read_missing_file():
    result = read_file("does_not_exist.txt")
    assert "Error" in result

def test_read_unsupported_format():
    result = read_file("file.pdf")
    assert "Error" in result


# ---------- calculate_statistics tests ----------

def test_calculate_statistics():
    result = calculate_statistics("test_sample.csv")
    assert "Average" in result
    assert "Score" in result

def test_calculate_statistics_missing_file():
    result = calculate_statistics("missing.csv")
    assert "Error" in result


# ---------- search_keywords tests ----------

def test_search_keyword_found():
    result = search_keywords("test_sample.txt", "error")
    assert "error found here" in result

def test_search_keyword_not_found():
    result = search_keywords("test_sample.txt", "banana")
    assert "No matches" in result


# ---------- summarise_text tests ----------

def test_count_lines():
    assert count_lines("line1\nline2\nline3") == 3

def test_count_words():
    assert count_words("one two three four") == 4

def test_preview_lines():
    result = preview_lines("a\nb\nc\nd\ne", 3)
    assert result == "a\nb\nc"