# Team Assignment Script

## Overview
This Python script reads an Excel file containing data on children (gender, age, height), sorts them, and assigns them to teams. The processed data is then saved into a new Excel file.

## Features
- Reads data from `Teams.xlsx`.
- Sorts children by **Gender**, **Age**, and **Height**.
- Counts the number of boys and girls.
- Assigns them into 4 teams as evenly as possible.
- Saves the updated data with assigned teams into `team_assignments.xlsx`.

## Requirements
- Python 3.6+
- Required libraries:
  ```bash
  pip install pandas openpyxl
  ```
- An Excel file named `Teams.xlsx` with appropriate column names.

## Usage
1. Ensure `Teams.xlsx` exists in the same directory as the script.
2. Run the script:
   ```bash
   python team_assignment.py
   ```
3. The output will be stored in `team_assignments.xlsx`.

## Expected Excel Format
| Name  | Gender | Age | Height |
|-------|--------|-----|--------|
| Alex  | Boy    | 12  | 150    |
| Sarah | Girl   | 13  | 155    |
| ...   | ...    | ... | ...    |

## Output File
A new Excel file `team_assignments.xlsx` will contain an additional **Team** column with assigned team numbers.

## Notes
- Ensure correct column names (`Gender`, `Age`, `Height`).
- Modify `boys_per_team` and `girls_per_team` calculation if different team sizes are needed.

## License
MIT License – Free to use and modify.
