import matplotlib.pyplot as plt

def treatment_pie_chart(df):
    try:
        ethnicity = input("Enter Ethnicity: ")
        filtered = df[df["Ethnicity"] == ethnicity]
        counts = filtered["Treatment"].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(counts, labels=counts.index, autopct="%1.1f%%")
        plt.title(f"Treatment Distribution for Ethnicity: {ethnicity}")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

def smoking_trend(df):
    try:
        ethnicities = df["Ethnicity"].unique()
        plt.figure(figsize=(10, 6))
        for eth in ethnicities:
            subset = df[df["Ethnicity"] == eth]
            avg = subset.groupby("Stage")["Smoking_Pack_Years"].mean()
            plt.plot(avg.index, avg.values, label=eth)
        plt.title("Smoking Pack Trend Across Cancer Stages")
        plt.xlabel("Cancer Stage")
        plt.ylabel("Avg Smoking Packs")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

def blood_pressure_comparison(df):
    try:
        avg_bp = df.groupby("Treatment")[
            ["Blood_Pressure_Systolic", "Blood_Pressure_Diastolic", "Blood_Pressure_Pulse"]
        ].mean()
        avg_bp.plot(kind="bar", figsize=(10, 6))
        plt.title("Avg Blood Pressure Types by Treatment")
        plt.ylabel("BP (mmHg)")
        plt.grid(axis="y")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

def survival_by_stage(df):
    try:
        avg_survival = df.groupby("Stage")["Survival_Months"].mean()
        avg_survival.plot(kind="bar", color="skyblue")
        plt.title("Average Survival Months by Tumor Stage")
        plt.ylabel("Avg Survival (Months)")
        plt.xlabel("Tumor Stage")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
