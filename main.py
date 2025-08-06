import argparse
import pandas as pd
import datetime




def colorCode(code):
    return f"\x1b[{code}m"

def calculateAge(DOB):
    format_string = "%Y-%m-%d"
    DOB = datetime.datetime.strptime(DOB, format_string)
    today = datetime.date.today()
    return today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))

def printStat(stat:str, low:float, high:float):
    if df[stat][0] < low:
        print(f"{colorCode(1)}{colorCode(107)}{colorCode(91)}{stat}: {colorCode(0)}{colorCode(107)}{colorCode(91)}{df[stat][0]}     {colorCode(1)}↓ {colorCode(0)}")
    elif df[stat][0] > high:
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
    
    for stat in df.columns:
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
            
            elif stat == "HeartRate_bpm":
                if age >= 18:
                    printStat("HeartRate_bpm", 60, 100)
                else:
                    printStat("HeartRate_bpm", 70, 130)
            elif stat == "SystolicBP_mmHg":
                if age >= 18:
                    printStat("SystolicBP_mmHg", 90, 120)
                else:
                    printStat("SystolicBP_mmHg", 80, 110)
            elif stat == "diastolicBP_mmHg":
                if age >= 18:
                    printStat("diastolicBP_mmHg", 90, 120)
                else:
                    printStat("diastolicBP_mmHg", 50, 75)
            elif stat == "RespiratoryRate_bpm":
                if age >= 18:
                    printStat("RespiratoryRate_bpm", 12, 20)
                else:
                    printStat("RespiratoryRate_bpm", 20, 30)
            elif stat == "Temperature_C":
                if age >= 18:
                    printStat("Temperature_C", 36.1, 37.2)
                else:
                    printStat("Temperature_C", 36.1, 37.8)
            elif stat == "SpO2_percent":
                printStat("SpO2_percent", 95, 100) #Kinda redundant since you can't have >100% SpO2

            elif stat == "Hemoglobin_g/dL":
                if age >= 18:
                    if df["Sex"][0] == "M":
                        printStat("Hemoglobin_g/dL", 13.8, 17.2)
                    elif df["Sex"][0] == "F":
                        printStat("Hemoglobin_g/dL", 12.1, 15.1)
                    else:
                        printStat("Hemoglobin_g/dL", 12.1, 17.2)
                else:
                    printStat("Hemoglobin_g/dL", 11, 16)
            elif stat == "WBC_10^3/uL":
                if age >= 18:
                    printStat("WBC_10^3/uL", 4.5, 11)
                else:
                    printStat("WBC_10^3/uL", 5, 15)
            elif stat == "Platelets_10^3/uL":
                printStat("Platelets_10^3/uL", 150, 450)
            elif stat == "BloodGlucose_mg/dL":
                printStat("BloodGlucose_mg/dL", 70, 140)
            elif stat == "SerumNa_mEq/L":
                printStat("SerumNa_mEq/L", 135, 145)
            elif stat == "SerumK_mEq/L":
                if age >= 18:
                    printStat("SerumK_mEq/L", 3.5, 5.1)
                else:
                    printStat("SerumK_mEq/L", 34, 4.7)
            elif stat == "Creatinine_mg/dL":
                if age >= 18:
                    if df["Sex"][0] == "M":
                        printStat("Creatinine_mg/dL", 0.74, 1.35)
                    elif df["Sex"][0] == "F":
                        printStat("Creatinine_mg/dL", 0.59, 1.04)
                else:
                    printStat("Creatinine_mg/dL", 0.3, 1)
            elif stat == "BUN_mg/dL":
                if age >= 18:
                    printStat("BUN_mg/dL", 7, 20)
                else:
                    printStat("BUN_mg/dL", 5, 18)



    
if __name__ == "__main__":
    main()
