import pandas as pd

def get_data(filename): 
    """Reads csv file and returns a dataframe."""
    data = pd.read_csv(filename)
    return data 
