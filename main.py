import argparse
import pandas as pd
import time

def colorCode(code):
    return f"\x1b[{code}m"

def main():
    parser = argparse.ArgumentParser(description="Process patient CSV file.")
    parser.add_argument(
        'csv_path',
        type=str,
        help='Path to the patient CSV file'
    )
    
    args = parser.parse_args()

    csv_path = args.csv_path

    df = pd.read_csv(csv_path)

    print(f"{colorCode(107)}{colorCode(90)}{colorCode(1)}{df["Surname"][0]}, {df["Name"][0]}     ({df["PatientID"][0]})")
    print(f"{df["DOB"][0]}     Sex: {df["Sex"][0]}{colorCode(0)}{colorCode(49)}{colorCode(39)}")
    print("")
    print("")
    print("")
    
    for stat in df[5:]:
        if df[stat].isnull().any():
            if stat == "Notes":
                print(f"{colorCode(107)}{colorCode(90)} No notes{colorCode(1)}")
            print(f"{colorCode(93)} {stat} missing. {colorCode(0)}")
        else:
            print(f"{colorCode(1)} {stat}:{colorCode(0)} {df[stat][0]}")



    
if __name__ == "__main__":
    main()