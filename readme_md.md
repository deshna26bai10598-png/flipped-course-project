# Age Calculator CLI

A simple, lightweight command-line application written in Python that calculates an individual's exact age in years based on their birth date and the current date.

Developed by **Deshna Jain**.

---

## Overview

Calculating exact age manually can be error-prone due to varying calendar month lengths and leap years. This project provides a quick, offline, and reliable command-line tool that automates age calculation while gracefully handling invalid inputs.

---

## Features

- **Exact Age Calculation:** Accurately computes age in years by comparing birth date tuples with current system dates.
- **Error Handling:** Protects against invalid numeric inputs or out-of-range calendar dates (e.g., February 30th or Month 13).
- **Zero Dependencies:** Built entirely with Python's standard `datetime` module—no external `pip` packages required.
- **Cross-Platform:** Runs seamlessly on Windows, macOS, and Linux terminals.

---

## Technologies & Tools

- **Language:** Python 3.x
- **Standard Library:** `datetime` (`date` class)

---

## Installation & Setup

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/deshnajain/age-calculator.git
   cd age-calculator
   ```

2. **Verify Python Installation:**
   Ensure Python 3 is installed on your machine:
   ```bash
   python --version
   ```

3. **Run the Application:**
   Execute the script directly from your terminal:
   ```bash
   python main.py
   ```

---

## Sample Execution

```text
Enter birth year (YYYY): 2004
Enter birth month (1-12): 5
Enter birth day (1-31): 18

You are 22 years old.
```

If invalid values are provided:

```text
Enter birth year (YYYY): 2023
Enter birth month (1-12): 2
Enter birth day (1-31): 30

Invalid date input. Please enter valid numbers.
```