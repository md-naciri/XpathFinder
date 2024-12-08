
# Xpath Finder

Xpath Finder is a Python-based utility designed to automate a repetitive task involving the processing of Excel files. 
This tool simplifies the process by matching data from a reference file with a target file and generating the required output. 

---

## Overview

This project was created to automate a repetitive task at my work. I noticed that processing and extracting Xpath data from Excel files was taking a lot of manual effort. To streamline this process, I wrote this program to automate the extraction and mapping of Xpath data from a reference file to a target file, which can be processed and saved with a new Xpath column.

---

## Features

- Select two Excel files: one reference and one to process.
- Automatically maps "Donnée du modèle" to "Xpath" from the reference file and appends it to the target file.
- Saves the processed file with a new "_output" suffix in the same directory as the processed file.

---

## Requirements

You need the following Python packages to run this program:

- **pandas**: For reading and processing Excel files.
- **openpyxl**: For handling Excel files (.xlsx format).

To install the necessary dependencies, run the following commands:

```bash
pip install pandas
pip install openpyxl
```
---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/XpathFinder.git
   cd XpathFinder
   ```

2. Ensure you have Python 3.x installed and a virtual environment set up (optional but recommended).

3. Install the required dependencies by running:
   ```
   pip install pandas
   pip install openpyxl
   ```

4. Run the program:
   ```bash
   python xpath_finder.py
   ```
   Follow the steps in the graphical interface:
   - Step 1: Select the reference Excel file.
   - Step 2: Select the Excel file to process.
   - Step 3: Click "Start Processing" to generate the output.

---

## Customization

If your Excel files have different column names, update the column references in the code:
- Replace `"Donnée du modèle"` with your source column name.
- Replace `"Xpath"` with your target column name.

---

## License

© 2024 md_naciri. All rights reserved.

---

## Contributions

Feel free to fork the repository, submit issues, or propose new features via pull requests.
