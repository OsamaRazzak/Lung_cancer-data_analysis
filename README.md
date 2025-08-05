

# Lung Cancer Analysis - Navdeep


This project is a modular Python-based analysis suite designed to study lung cancer patient data using statistical and visual methods. The analysis is performed via scripts and a Jupyter Notebook for interactivity.

## Features

- Load and clean patient data from CSV
- Perform separate analysis tasks:
  - Task A: Demographics and medical history
  - Task B: Risk detection (age, cancer stage, BP)
  - Task C: Treatment outcomes and visual summaries
- Generate visualizations:
  - Smoking vs Stage analysis
  - Treatment type distribution
  - Blood pressure and survival comparisons

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/lung-cancer-analysis.git
   cd lung-cancer-analysis
   ```

2. Install the required Python packages:

   ```bash
   pip install pandas matplotlib notebook
   ```

3. Run the Jupyter Notebook:

   ```bash
   jupyter notebook main.ipynb
   ```

4. Follow the menu prompts in the notebook to interact with the data.

## Project Structure

```text
lung-cancer-analysis-navdeep/
├── src/
│   ├── data/                # Raw or processed data files (e.g., CSV)
│   ├── task_a.py            # Demographics and history analysis
│   ├── task_b.py            # High-risk patient detection
│   └── task_c.py            # Treatment and survival analysis
├── main.ipynb               # Main interactive Jupyter Notebook
├── requirements.txt         # Required Python packages
└── .gitignore

```

## CSV Format

Make sure your CSV file contains the following columns (or similar):

- Patient_ID
- Age
- Gender
- Smoking_History
- Stage
- Treatment
- Survival_Months
- Blood_Pressure_Systolic
- Blood_Pressure_Diastolic
- Blood_Pressure_Pulse
- Haemoglobin_Level
- White_Blood_Cell_Count
- Ethnicity
- Tumor_Size_mm
- Tumor_Location
- Family_History
- Comorbidity_Diabetes
- Comorbidity_Kidney_Disease
- Smoking_Pack_Years

## Requirements

- Python 3.7 or higher
- Jupyter Notebook
- pandas
- matplotlib

Install the required packages with:

```bash
pip install pandas matplotlib notebook
```
# Lung_cancer-data_analysis
