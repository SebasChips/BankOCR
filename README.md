# BankOCR## Table of Contents
1. [General Info](#general-info)
2. [How to use it?](#operation)

### General Info
***
This project resolves de Bank OCR project. The problems says:
In this programming challenge, the task is to develop a program that can process a scanned or photographed check's machine-readable line, extracting and validating a 9-digit account number. The machine-readable line is represented by a series of characters, each encoded in a 3x3 grid of segments.

Each character can be one of the digits from 0 to 9. To ensure the correctness of the account number, a validation check should be included in the program. The provided validation formula is:

Checksum=((d9×1)+(d8×2)+(d7×3)+(d6×4)+(d5×5)+(d4×6)+(d3×7)+(d2×8)+(d1×9))mod11. Where d represents the positions of the numbers in the bank account.

## How to use it?
***
1. Clone the repository where you want it to have. git clone https://github.com/SebasCips/BankOCR
2. Run from the terminal the next command: python main.py
3. Check for a new file named "bankAccounts.txt" in there you can see if the accounts where approved
