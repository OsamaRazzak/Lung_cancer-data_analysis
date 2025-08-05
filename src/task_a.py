import csv

def load_data(file_path):
    try:
        with open(file_path, newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [dict(zip(header, row)) for row in reader]
        return data
    except FileNotFoundError:
        print("File not found please check the path")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_demographic_info(data):
    try:
        patient_id = input("Enter Patient_ID: ")
        for row in data:
            if row["Patient_ID"] == patient_id:
                return {
                    "Age": row["Age"],
                    "Gender": row["Gender"],
                    "Smoking_History": row["Smoking_History"],
                    "Ethnicity": row["Ethnicity"],
                }
    except Exception as e:
        print(f"An error occurred: {e}")

def get_med_hist_by_ethnicity(data):
    try:
        ethnicity = input("Enter Ethnicity: ")
        return [
            {
                "Patient_ID": row["Patient_ID"],
                "Family_History": row["Family_History"],
                "Comorbidity_Diabetes": row["Comorbidity_Diabetes"],
                "Comorbidity_Kidney_Disease": row["Comorbidity_Kidney_Disease"],
                "Haemoglobin_Level": row["Haemoglobin_Level"],
            }
            for row in data
            if row["Ethnicity"] == ethnicity
        ]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def long_survivors(data):
    try:
        treatment_name = input("Enter Treatment: ")
        return [
            {
                "Age": row["Age"],
                "Tumor_Size_mm": row["Tumor_Size_mm"],
                "Tumor_Location": row["Tumor_Location"],
                "Stage": row["Stage"],
            }
            for row in data
            if row["Treatment"] == treatment_name and float(row["Survival_Months"]) > 100
        ]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def high_risk_patients(data):
    try:
        return [
            {
                "Patient_ID": row["Patient_ID"],
                "Age": row["Age"],
                "Stage": row["Stage"],
                "Blood_Pressure_Systolic": row["Blood_Pressure_Systolic"],
            }
            for row in data
            if int(row["Age"]) > 60
            and row["Stage"] == "Stage III"
            and float(row["Blood_Pressure_Systolic"]) > 130
        ]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
