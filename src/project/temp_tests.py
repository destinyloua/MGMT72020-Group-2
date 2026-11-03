# from src.project.descriptive_functions import get_data, get_category_count
# from src.project.patient_info import Patient

from descriptive_functions import get_data, get_category_count
from patient_info import Patient

FILENAME = "../data/lung_cancer_dataset.csv"

test_data = {
    'Column1': ['a', 'b', 'c', 'a'], 
    'Column2': ['b', 'b', 'c', 'a']
} 

df = get_data(FILENAME)

def test_01_category_count(category): 
    """Checks category count function returns sum correctly."""
    assert get_category_count('Column1') == ({'a': 2, 'b': 1, 'c': 1})

def test_02_check_patient_count(): 
    """Checks all 2000 patients were loaded into a list."""
    p = Patient(df)
    assert len(p.create_patient_list) == 2000

