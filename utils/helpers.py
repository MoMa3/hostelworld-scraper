import re


def extract_number(text):
    """
    Extract and return the first number found in the input text.

    Args:
    text (str): The input text containing numbers.

    Returns:
    float: The extracted number, or None if no number is found.
    """
    match = re.search(r"\d+(\.\d+)?", text)

    if match:
        return float(match.group())
    else:
        return None

def create_object(**kwargs):
    return kwargs
