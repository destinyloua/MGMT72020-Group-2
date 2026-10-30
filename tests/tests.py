# UNIT TESTS FOR TDD 
# import sys 
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from ..src.descriptive_functions import get_category_count, get_data
from ..src.patient_info import Patient

test_data = {
    'Column1': ['a', 'b', 'c', 'a'], 
    'Column2': ['b', 'b', 'c', 'a']
} 

df = get_data("../data/lung_cancer_dataset.csv")

def test_01_category_count(category): 
    """Checks category count function returns sum correctly."""
    assert get_category_count('Column1') == ({'a': 2, 'b': 1, 'c': 1})

def test_02_check_patient_count(): 
    """Checks all 2000 patients were loaded into a list."""
    p = Patient(df)
    assert len(p.create_patient_list) == 2000

