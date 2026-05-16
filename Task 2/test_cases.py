from detector import classify_answer

# Test Cases
test_cases = [

    ("Machine learning is part of AI", "valid"),

    ("hello", "irrelevant"),

    ("aaaaaaa!!!!!!", "spam"),

    ("", "empty"),
    
    ("$$$$$$$", "spam"),

    ("Artificial Intelligence helps machines learn", "valid")
]

# Run Test Cases
print("\n===== TEST CASE RESULTS =====\n")

for answer, expected in test_cases:

    result = classify_answer(answer)

    print(f"Input: {answer}")

    print(f"Expected Output: {expected}")

    print(f"Predicted Output: {result}")

    print("-----------------------------------")