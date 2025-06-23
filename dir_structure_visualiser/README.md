## Introduction

The CLI script takes a path to a folder as an argument and prints a colorized tree representation of its file structure, distinguishing folders and files with different colors.

## Usage

CLI command:
```python main.py ./mock/test-folder```

## Structure

- main.py – entry point of the script
- utils/ – global constants and shared helper functions
- handlers/ – core logic and handler methods; may include local utils.py for handler-specific helpers
- mock/ – test or demo data used for local testing
- requirements.txt – list of external dependencies required to run the project;

## Output example
test-folder/
        file2.txt
        file1.txt
        folder2/
        folder1/
            file3.txt
            folder3/
                file4.txt
                file5.txt
                folder5/
                    file8.txt
            folder4/
                file7.txt
                file6.txt