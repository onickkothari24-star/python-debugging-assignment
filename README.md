# Python Debugging Assignment

## Project Overview
This project demonstrates Python debugging and unit testing. It contains a Python script with three intentional bugs and a test file used to verify the corrected functions.

## Project Files
- `buggy_script.py` — contains functions to calculate an average, find the largest number, and count even numbers.
- `test_buggy_script.py` — contains unit tests for these functions.
- `README.md` — provides project and execution instructions.

## Requirements
- Python 3
- No external Python packages are required.

## Setup Instructions
1. Download and extract the project files.
2. Open the project folder in Cursor or another Python editor.
3. Open a terminal in the project folder.

## Run the Python Program
Execute the following command:

```bash
python buggy_script.py
```

## Run the Unit Tests
Execute:

```bash
python -m unittest -v
```

The tests check the average calculation, largest-number calculation with negative values, and even-number counting, including an average calculated from a single number.

Fix the intentional bugs in `buggy_script.py` and run the tests again to verify the corrections.

## Conclusion
This project provides practice in identifying Python errors, making corrections, running automated unit tests, and documenting code.
