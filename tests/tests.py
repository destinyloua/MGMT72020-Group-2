# UNIT TESTS FOR TDD 
#import unittest
import pytest

class TestLoadData:
    def test_load_data(self): 
        """Checks that the data is loaded correctly."""
        from project import get_data
        df = get_data("../data/lung_cancer_dataset.csv")
        assert df.shape == (2000, 14)  # Assuming the dataset has 2000 rows and 14 columns

# from project import descriptive_functions as d
# from project import patient_info

# test_data = {
#     'Column1': ['a', 'b', 'c', 'a'], 
#     'Column2': ['b', 'b', 'c', 'a']
# } 

# # df = get_data("../data/lung_cancer_dataset.csv")

# class Test01_Category_Count(unittest.TestCase):
#     def test_01_category_count(self): 
#         """Checks category count function returns sum correctly."""
#         self.assertEqual(d.get_category_count('Column1'), ({'a': 2, 'b': 1, 'c': 1})) 

# # def test_02_check_patient_count(): 
# #     """Checks all 2000 patients were loaded into a list."""
# #     p = Patient(df)
# #     assert len(p.create_patient_list) == 2000

# if __name__ == "__main__": 
#     unittest.main()
