import sqlite3
import pandas as pd

def get_lung_cancer_data(): 
    """Reads data from sqlite database and returns a dataframe."""
    con = sqlite3.connect("../data/lung_cancer.db")
    data = pd.read_sql_query("SELECT * from lung_cancer", con)
    con.close()
    return data

def get_data(filename):
    """Reads csv file and returns a dataframe."""
    data = pd.read_csv(filename)
    return data 
