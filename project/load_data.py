import sqlite3
import pandas as pd

def get_lung_cancer_data(): 
    con = sqlite3.connect("../data/lung_cancer.db")
    data = pd.read_sql_query("SELECT * from lung_cancer", con)
    con.close()
    return data

def get_data(filename):
    """Reads csv file and returns a dataframe."""
    data = pd.read_csv(filename)
    return data 



# def create_patients(data):
#     """Returns a list of patient objects."""
#     pass 

# def get_patient_chars(df): 
#     """Returns a dataframe with patient characteristics only."""
#     patient_df = df.copy() 
#     return patient_df.filter(items=["Gender", "Age", "Country", "Family History"])

# def get_category_count(category, data):
#     """Returns a count of the number of patients in each category."""
#     return data[category].value_counts(dropna=True)
