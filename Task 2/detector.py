import re

# Empty Detection
def is_empty(answer):

    # Handle None input
    if answer is None:
        return True

    # Remove spaces, tabs, newlines
    cleaned_answer = answer.strip()

    return cleaned_answer == ""

# Spam Detection
def is_spam(answer):

    # Repeated characters
    if re.search(r'(.)\1{5,}', answer):
        return True

    # Only special characters
    if re.fullmatch(r'[^a-zA-Z0-9]+', answer):
        return True

    return False

# Irrelevant Detection
def is_irrelevant(answer):

    words = answer.split()

    # Very short answers
    if len(words) < 2:
        return True

    return False

# Main Classification Logic
def classify_answer(answer):

    # EMPTY CHECK FIRST
    if is_empty(answer):
        return "empty"

    # SPAM CHECK
    elif is_spam(answer):
        return "spam"

    # IRRELEVANT CHECK
    elif is_irrelevant(answer):
        return "irrelevant"

    # VALID ANSWER
    else:
        return "valid"