import pandas as pd

def get_data(filename): 
    """Reads csv file and returns a dataframe."""
    data = pd.read_csv(filename)
    return data 

def get_patient_chars(df): 
    """Returns a dataframe with patient characteristics only."""
    patient_df = df.copy() 
    return patient_df.filter(items=["Gender", "Age", "Country", "Family History"])

