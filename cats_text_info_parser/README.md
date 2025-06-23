## Introduction

The script reads a cats_file.txt containing id, name and age of list of cats, and returns an array of dictionaries: [{ "id": "1", "name": "Tom", "age": "3"}, ...].

## Usage

Place cats_file.txt in the project root directory and run the program.

## Structure

- main.py – entry point of the script
- utils/ – global constants and shared helper functions
- handlers/ – core logic and handler methods; may include local utils.py for handler-specific helpers