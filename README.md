# README for Python Cut Tool

## Overview
This project includes a Python implementation of the Unix `cut` command, named `pycut`. The script is designed to mimic the functionality of the Unix `cut` tool, allowing users to select portions of each line from a given file or standard input, using a specified delimiter and field numbers.

## Features
- **Field Selection**: Select specific fields from each line of the file or standard input.
- **Custom Delimiters**: Choose a custom delimiter character for separating fields in a line.
- **Standard Input Support**: Ability to read from standard input if no file is specified or if a dash (`-`) is provided as the file name.
- **Command-Line Interface**: Fully functional command-line interface for easy use in Unix-like environments.

## Requirements
- Python 3.x

## Installation
No installation is needed. Just ensure Python 3.x is installed on your system.

## Usage
Run the script from the command line, specifying the options for field selection and delimiter. 

### Basic Usage
```
python pycut.py -f <fields> -d <delimiter> [file]
```
- `<fields>`: Comma-separated list of field numbers to select.
- `<delimiter>`: Delimiter character to use for splitting the fields.
- `[file]`: Optional. Path to the file to be processed. If omitted, the script reads from standard input.

### Examples
1. Selecting the second field from a file with a comma delimiter:
   ```
   python pycut.py -f 2 -d "," yourfile.csv
   ```

2. Reading from standard input and selecting fields 1 and 2:
   ```
   cat sample.tsv | python pycut.py -f 1,2
   ```

## Combining with Other Unix Commands (Windows Subsystem for Linux or Unix-like systems only)
The Python `cut` tool can be combined with other Unix commands to create data processing pipelines.

Example: Counting the number of unique artists in a dataset.
```
python pycut.py -f 2 -d "," fourchords.csv | sort | uniq | wc -l
```

## Notes for Windows Users
- The `sort`, `uniq`, and `wc` commands might not be available in standard Windows command line environments.
- Use Windows Subsystem for Linux (WSL), Git Bash, or PowerShell to execute Unix-like commands.
- In PowerShell, you can replace `sort | uniq | wc -l` with `Sort-Object | Get-Unique | Measure-Object -Line`.

