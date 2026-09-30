# STATEMENT.md: Age Calculator Problem & Scope Statement

**Student Name:** Deshna Jain  
**Project Title:** Automated Age Calculator CLI  

---

## 1. Problem Statement
Manual calculation of an individual's exact age requires accounting for month differences, day boundaries, and leap year cycles. Online calculators and GUI-based tools often require active internet connections, display intrusive advertisements, or introduce unnecessary software dependencies. 

There is a need for a minimalist, dependency-free, offline command-line utility that can accurately evaluate date differences and yield instantaneous age output while safeguarding against invalid input errors.

---

## 2. Scope of the Project

### In-Scope:
- Interactive command-line interface for gathering user birth year, month, and day.
- Precise calculation of current age in years using system date benchmarking.
- Automatic adjustment for birth dates that have not yet occurred in the current calendar year.
- Input validation to catch `ValueError` exceptions caused by malformed inputs or non-existent dates.

### Out-of-Scope:
- Web-based user interfaces or desktop GUIs.
- Detailed breakdown down to total minutes, hours, or seconds.
- Multi-user data storage or database integration.

---

## 3. Target Audience
- **Students & Educators:** Needing a quick reference implementation for date handling in Python programming assignments.
- **Utility Users:** Individuals seeking a quick, ad-free, offline terminal utility for age verification.

---

## 4. High-Level Features
- **Lightweight & Fast:** Executes instantly (< 10ms execution time).
- **Robust Exception Handling:** Prevents runtime crashes using structured `try-except` validation blocks.
- **Standard Library Driven:** Operates natively within standard Python runtimes without third-party libraries.