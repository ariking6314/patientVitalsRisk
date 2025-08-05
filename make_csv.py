import csv

header = ['PatientID', 'Surname', 'Name', 'DOB', 'Sex', 'HeartRate_bpm', 'SystolicBP_mmHg', 'DiastolicBP_mmHg', 'RespiratoryRate_bpm', 'Temperature_C', 'SpO2_percent', 'Hemoglobin_g/dL', 'WBC_10^3/uL', 'Platelets_10^3/uL', 'BloodGlucose_mg/dL', 'SerumNa_mEq/L', 'SerumK_mEq/L', 'Creatinine_mg/dL', "BUN_mg/dL", "Notes"]

#Demographics and Identification
patientID = input("Patient ID: ")
surname = input("Surname: ").upper()
name = input("First Name: ").upper()
dob = input("Date of Birth (YYYY-MM-DD): ")
sex = input("Sex (M/F): ")

#Vitals
hr = input("Heart Rate (bpm): ")
sbp = input("Systolic Blood Pressure (mmHg): ")
dbp = input("Diastolic Blood Pressure (mmHg): ")
rr = input("Respiratory Rate (bpm): ")
temp = input("Temperature (°C): ")
spo2 = input("SpO2 (%): ")

#CBC
hb = input("Hemoglobin (g/dL): ")
wbc = input("Whtie Blood Count (10³/uL): ")
platelets = input("Platelets (10³/uL): ")

#BMP
glucose = input("Blood Glucose: (mg/dL): ")
na = input("Serum Sodium (mEq/L): ")
k = input("Serum Potassium (mEq/L): ")
cr = input("Creatinine (mg/dL): ")
bun = input("Blood Urea Nitrogen (mg/dL): ")

#NOTES
note = input("Note: ")


data = [patientID, surname, name, dob, sex, hr, sbp, dbp, rr, temp, spo2, hb, wbc, platelets, glucose, na, k, cr, bun, note]


if not name:
        print("MISSING FIRST NAME")
        name = "UNKNOWN_NAME"
    
if not surname:
        print("MISSING SURNAME")
        surname = "UNKNOWN_SURNAME"
    
if not patientID:
        print("MISSING PATIENT ID")
        patientID = "UNKNOWN_PATIENT_ID"
    
csv_file_path = f'{surname}, {name} - {patientID}.csv'
    
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(header)
    writer.writerow(data)

print(f"CSV File created: {csv_file_path}")