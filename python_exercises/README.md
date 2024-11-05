# Python Exercises
This repository contains solutions to various Python exercises.

Base one the question below:

![alt text](python_exercise.png)
---
# My Python Tasks

This repository contains solutions for two Python tasks involving dictionary manipulation. Each task has its own Python module for separation and ease of testing. 

## Table of Contents
1. [Task 1: Sort Dictionary Keys Alphabetically](#task-1-sort-dictionary-keys-alphabetically)
2. [Task 2: Save and Load Dictionary from a File](#task-2-save-and-load-dictionary-from-a-file)
<!-- 3. [Project Structure](#project-structure) -->
4. [How to Run Task1](#how-to-run-task1)
4. [How to Run Task2](#how-to-run-task2)

---

## Task 1: Sort Dictionary Keys Alphabetically

### Description
This task requires a function that:
1. Takes a dictionary (or JSON input).
2. Sorts all its keys alphabetically.
3. Returns the sorted dictionary.

The sorting applies recursively to nested dictionaries, so all levels of the dictionary will be sorted by their keys in alphabetical order.

### Code Reference
- Module: `tasks/sort_dictionary.py`
- Key Function: `sort_dictionary(input_dict: dict) -> dict`
- Python Modules Used:
  - `json`: Used to parse JSON strings if needed, though this task primarily manipulates Python dictionaries directly.

### Example Usage
```python
from tasks.sort_dictionary import sort_dictionary

input_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "postalCode": "12345"
    },
    "phoneNumbers": [
        {"type": "home", "number": "123-456-7890"},
        {"type": "work", "number": "987-654-3210"}
    ]
}

sorted_dict = sort_dictionary(input_dict)
print(sorted_dict)
```

---

## How to Run Task1

1. Clone this repository
2. Install Python 3.8 or higher
3. Install the `pytest` package
4. Run the following command: `pytest tasks/sort_dictionary.py`

---



## Task 2: Save and Load Dictionary from a File



## How to Run Task2