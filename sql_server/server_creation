import sqlite3
import csv
import sys
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# import load data module from project folder
from project.load_data import get_data
FILENAME = PROJECT_ROOT / "data" / "lung_cancer_dataset.csv"

# def get_data(filename): 
#     """Reads csv file and returns a dataframe."""
#     data = pd.read_csv(filename)
#     return data 

data = get_data(FILENAME)
conn = sqlite3.connect('data/lung_cancer.db')

cursor = conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS lung_cancer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Patient_ID TEXT,
    Diagnosis_Year INTEGER,
    Diagnosis_Date TEXT,
    WHO_Region TEXT,
    Country TEXT,
    Age INTEGER,
    Age_Group TEXT,
    Gender TEXT,
    Smoking_Status TEXT,
    Cigarettes_Per_Day INTEGER,
    Years_Smoking INTEGER,
    Pack_Years INTEGER,
    Secondhand_Smoke TEXT,
    Family_History TEXT,
    Occupational_Hazard TEXT,
    Air_Pollution_Exposure TEXT,
    Alcohol_Use INTEGER,
    BMI REAL,
    BMI_Category TEXT,
    Exercise_Frequency TEXT,
    Chronic_Lung_Disease TEXT,
    Asbestos_Exposure TEXT,
    Radon_Exposure TEXT,
    Previous_Cancer_History TEXT,
    Risk_Factor_Count INTEGER,
    Genetic_Mutation TEXT,
    Coughing TEXT,
    Shortness_of_Breath TEXT,
    Chest_Pain TEXT,
    Coughing_Blood TEXT,
    Fatigue TEXT,
    Weight_Loss TEXT,
    Wheezing TEXT,
    Recurrent_Infections TEXT,
    Swallowing_Difficulty TEXT,
    Finger_Clubbing TEXT,
    Symptom_Count INTEGER,
    Cancer_Type TEXT,
    NSCLC_Subtype TEXT,
    Cancer_Stage TEXT,
    Tumor_Size_cm REAL,
    Metastasis TEXT,
    Diagnosis_Method TEXT,
    Treatment TEXT,
    Survival_Months INTEGER,
    Survived INTEGER)'''


# file = open(data)

# contents = csv.reader(file)

#insert_records = 'INSERT INTO lung_cancer VALUES (?)'
data.to_sql("lung_cancer", conn, if_exists="replace", index=False)


#cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM lung_cancer"
rows = cursor.execute(select_all).fetchall()

preview = "SELECT * FROM lung_cancer LIMIT 1"
get_preview = cursor.execute(preview).fetchall()

# Output to the console screen
# for r in rows:
#     print(r)

print(f"{get_preview}")
conn.close()
