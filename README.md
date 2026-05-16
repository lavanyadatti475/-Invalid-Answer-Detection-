# Invalid Answer Detection Module

## Overview

The Invalid Answer Detection Module is a rule-based NLP system developed as part of the Evaluation Engine. The module automatically detects and classifies user responses into four categories:

- Valid
- Irrelevant
- Spam
- Empty

The project helps improve evaluation quality by filtering meaningless, unrelated, or spam responses before assessment.

---

# Features

- Automatic answer classification
- Spam detection
- Empty answer detection
- Irrelevant answer identification
- Flask API integration
- Frontend and backend integration
- Edge case handling
- Test case validation

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web framework/API |
| HTML | Frontend structure |
| CSS | Styling |
| Regex | Spam detection |
| VS Code | Development environment |

---

# Project Structure

```text
invalid_answer_detection/
│
├── app.py
├── detector.py
├── test_cases.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
````

---

# Installation

## Step 1: Clone Repository

```bash
git clone <repository-link>
```

---

## Step 2: Navigate to Project Folder

```bash
cd invalid_answer_detection
```

---

## Step 3: Install Required Libraries

```bash
pip install flask
```

---

# Running the Project

Run the application using:

```bash
python app.py
```

---

# Open Browser

```text
http://127.0.0.1:5000
```

---

# API Details

## Endpoint

```text
/detect
```

## Method

```text
POST
```

---

# Sample API Input

```json
{
  "answer": "Machine learning is part of AI"
}
```

---

# Sample API Output

```json
{
  "classification": "valid"
}
```

---

# Classification Logic

| Classification | Description            |
| -------------- | ---------------------- |
| valid          | Meaningful answer      |
| irrelevant     | Short/unrelated answer |
| spam           | Repeated/random text   |
| empty          | Blank input            |

---

# Example Outputs

| Input                             | Output     |
| --------------------------------- | ---------- |
| Artificial Intelligence is useful | valid      |
| hello                             | irrelevant |
| aaaaaaa!!!!!!                     | spam       |
| (empty input)                     | empty      |

---

# Edge Cases Handled

* Whitespace inputs
* Tabs and newlines
* Repeated characters
* Special character spam
* Very short answers
* False positive reduction

---

# Test Cases

Run test cases using:

```bash
python test_cases.py
```

---

# Sample Test Results

| Test Input             | Expected Output |
| ---------------------- | --------------- |
| Machine learning is AI | valid           |
| hello                  | irrelevant      |
| !!!!!!!!               | spam            |
| ""                     | empty           |

---

# Workflow

```text
User Answer
      ↓
Text Processing
      ↓
Detection Logic
      ↓
Classification Result
      ↓
Frontend/API Response
```

---

# Results

The system successfully classifies user answers into valid, irrelevant, spam, and empty categories while handling edge cases effectively.

---

# Future Enhancements

* Machine Learning integration
* Advanced NLP models
* Database integration
* User authentication
* Real-time analytics
* Semantic similarity checking

---

# Conclusion

The Invalid Answer Detection Module provides an efficient solution for filtering invalid user responses in evaluation systems. The project improves assessment reliability and demonstrates practical implementation of rule-based NLP classification using Python and Flask.

```
```
