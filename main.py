import argparse
import pandas as pd
import datetime

ranges = {
    "HeartRate_bpm": {
        "adult_male": (60, 100),
        "adult_female": (60, 100),
        "adult": (60, 100),
        "pediatric": (70, 130),
    },
    "SystolicBP_mmHg": {
        "adult_male": (90, 120),
        "adult_female": (90, 120),
        "adult": (90, 120),
        "pediatric": (80, 110),
    },
    "DiastolicBP_mmHg": {
        "adult_male": (60, 80),
        "adult_female": (60, 80),
        "adult": (60, 80),
        "pediatric": (50, 80),
    },
    "RespiratoryRate_bpm": {
        "adult_male": (12, 20),
        "adult_female": (12, 20),
        "adult": (12, 20),
        "pediatric": (20, 30)
    },
    "Temperature_C": {
        "adult_male": (36.1, 37.2),
        "adult_female": (36.1, 37.2),
        "adult": (36.1, 37.2),
        "pediatric": (36.1, 37.2)
    },
    "SpO2_percent": {
        "adult_male": (95, 100),
        "adult_female": (95, 100),
        "adult": (95, 100),
        "pediatric": (95, 100)
    },
    "Hemoglobin_g/dL": {
        "adult_male": (13.5, 17.5),
        "adult_female": (12.0, 15.5),
        "adult": (12.0, 17.5),
        "pediatric": (11.0, 16),
    },
    "WBC_10^3/uL": {
        "adult_male": (4.5, 11),
        "adult_female": (4.5, 11),
        "adult": (4.5, 11),
        "pediatric": (5, 13)
    },
    "Platelets_10^3/uL": {
        "adult_male": (150, 450),
        "adult_female": (150, 450),
        "adult": (150, 450),
        "pediatric": (150, 450)
    },
    "BloodGlucose_mg/dL": {
        "adult_male": (70, 99),
        "adult_female": (70, 99),
        "adult": (70, 99),
        "pediatric": (70, 99)  
    },
    "SerumNa_mEq/L": {
        "adult_male": (135, 145),
        "adult_female": (135, 145),
        "adult": (135, 145),
        "pediatric": (135, 145)
    },
    "SerumK_mEq/L": {
        "adult_male": (3.5, 5),
        "adult_female": (3.5, 5),
        "adult": (3.5, 5),
        "pediatric": (3.4, 4.7)
    },
    "Creatinine_mg/dL": {
        "adult_male": (0.74, 1.35),
        "adult_female": (0.59, 1.04),
        "adult": (0.74, 1.35),
        "pediatric": (0.2, 1.0),
    },
    "BUN_mg/dL": {
        "adult_male": (7, 20),
        "adult_female": (7, 20),
        "adult": (7, 20),
        "pediatric": (5, 18)
    },
}


def colorCode(code):
    return f"\x1b[{code}m"

def calculateAge(DOB):
    format_string = "%Y-%m-%d"
    DOB = datetime.datetime.strptime(DOB, format_string)
    today = datetime.date.today()
    return today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))

def printStat(stat: str, demographic: str):
    if df[stat][0] > ranges[stat][demographic][1]:
        print(f"{colorCode(1)}{colorCode(107)}{colorCode(91)}{stat}: {colorCode(0)}{colorCode(107)}{colorCode(91)}{df[stat][0]}     {colorCode(1)}↓ {colorCode(0)}")
    elif df[stat][0] < ranges[stat][demographic][0]:
        print(f"{colorCode(1)}{colorCode(107)}{colorCode(91)}{stat}: {colorCode(0)}{colorCode(107)}{colorCode(91)}{df[stat][0]}     {colorCode(1)}↑ {colorCode(0)}")
    else:
        print(f"{colorCode(1)} {stat}:{colorCode(0)} {df[stat][0]}{colorCode(0)}")


def main():
    parser = argparse.ArgumentParser(description="Process patient CSV file.")
    parser.add_argument(
        'csv_path',
        type=str,
        help='Path to the patient CSV file'
    )
    
    args = parser.parse_args()

    csv_path = args.csv_path

    global df
    df = pd.read_csv(csv_path)


    print(f"{colorCode(107)}{colorCode(90)}{colorCode(1)}{df['Surname'][0]}, {df['Name'][0]}     ({df['PatientID'][0]})")

    try:
        age = calculateAge(df['DOB'][0])
    except TypeError:
        age = f"{colorCode(93)}DOB Missing{colorCode(0)}"
    
    print(f"{df['DOB'][0]} ({age})     Sex: {df['Sex'][0]}{colorCode(0)}")
    print("")
    print("")
    print("")
    
    for stat in df.columns[5:]:
        if df[stat].isnull().any(): #Handles Missing Data
            if stat == "Notes":
                print("")
                print(f"{colorCode(107)}{colorCode(90)} No notes{colorCode(0)}")
            else:
                print(f"{colorCode(93)} {stat} missing. {colorCode(0)}")
        else: #Handles the data that has been inputed
            if stat == "Notes":
                print("")
                print(f"{colorCode(107)}{colorCode(90)} {df[stat][0]}{colorCode(0)}")
            else:
                if age <= 18:
                    printStat(stat, "pediatric")
                else:
                    if df["Sex"][0] == "M":
                        printStat(stat, "adult_male")
                    elif df["Sex"][0] == "F":
                        printStat(stat, "adult_female")
                    else:
                        printStat(stat, "adult")



    
if __name__ == "__main__":
    main()
