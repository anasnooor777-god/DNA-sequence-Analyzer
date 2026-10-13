
# DNA Sequence Analyzer

A modular Python program for analyzing and processing DNA sequences.

## Features

- Validates DNA sequences
- Counts each nucleotide (A, T, G, C)
- Generates the complementary DNA strand
- Handles lowercase input
- Includes automated unit tests

## Technologies Used

- Python 3
- Python unittest

## How to Run

1. Install Python 3.
2. Open the project folder in your terminal.
3. Run the program:

```bash
python dna_analyzer.py
```

## Example

Input:

```text
ATGCAT
```

Output:

```text
Valid DNA sequence!
Nucleotide counts: {'A': 2, 'T': 2, 'G': 1, 'C': 1}
Complementary strand: TACGTA
```

## Run Tests

Run the automated tests using:

```bash
python -m unittest test_dna_analyzer
```

## Project Purpose

This project demonstrates modular programming, string processing, DNA sequence validation, nucleotide counting, complementary strand generation, and automated testing in Python.