import pandas as pd

def load_dataframe(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"

def top_treatments_by_ethnicity(df):
    ethnicity = input("Enter Ethnicity: ").strip()
    try:
        df["Survival_Months"] = df["Survival_Months"].astype(int)
        filtered = df[(df["Ethnicity"] == ethnicity) & (df["Survival_Months"] > 100)]
        top_treatments = filtered["Treatment"].value_counts().head(3)
        if top_treatments.empty:
            return f"No high-survival patients found for ethnicity '{ethnicity}'."
        return top_treatments
    except Exception as e:
        return f"Error: {e}"

def avg_wbc_by_treatment(df):
    try:
        ethnicity = input("Enter Ethnicity: ")
        filtered = df[df["Ethnicity"] == ethnicity]
        return filtered.groupby("Treatment")["White_Blood_Cell_Count"].mean()
    except Exception as e:
        return f"Error: {e}"

def smoking_analysis(df):
    try:
        filtered = df[(df["Blood_Pressure_Pulse"] > 90) & (df["Tumor_Size_mm"] < 15.0)]
        return filtered.groupby(["Treatment", "Tumor_Location"])[
            "Smoking_Pack_Years"
        ].mean()
    except Exception as e:
        return f"Error: {e}"

def survival_and_haemoglobin_by_ethnicity(df):
    try:
        return df.groupby("Ethnicity")[["Survival_Months", "Haemoglobin_Level"]].mean()
    except Exception as e:
        return f"Error: {e}"
