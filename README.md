# Patient Vitals Risk Assesment CLI
A simple, stylish command-line tool that reads in patient vitals from a CSV and flags health risks based on age and sex-specific reference ranges. 

- Built with Python
- Intended for terminal usage
- CSV-based data input
- ANSI color-coded output for quick visual scanning
- Clinical data ranges used: Heart rate, BP, CBC, BMP

## Project Structure

```
patientVitalsRisk/
├── make_csv.py     # Interactive CLI to create a patient CSV
├── main.py         # Analyzes patient data and prints warnings
├── *.csv           # Patient files (e.g., "WILLIAMS, JORDAN - 0001.csv")
```

## Setup
### Requirements
- Python 3.6+
- `pandas`


Install dependencies:

`pip install pandas`

## Usage
### Create patient CSV:
`python make_csv.py`

You'll be prompted for:

- Demographics
- Vitals
- Lab results
- Optional Notes

A CSV file will be saved in the format: 
`SURNAME, NAME - PATIENTID.csv`

### Analyze the patient data:
`python main.py "[DOE, JOHN - #.csv]"`

This will return a color-coded readout of the patient's health status. Alerts include:
- Out of range vitals/labs (↑ or ↓)
- Missing data
- Optional Notes

Supports age-based and sex-based reference ranges

## Example output:
`python main.py "WILLIAMS, JORDAN - P001.csv"`

This will return the following

![Console output](https://raw.githubusercontent.com/ariking6314/patientVitalsRisk/refs/heads/main/image.png)
