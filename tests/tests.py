# UNIT TESTS FOR TDD 
import unittest
import sys
import pandas as pd
from pathlib import Path
from project import load_data as l
from project import descriptive_summary as ds 

# PROJECT_ROOT = Path(__file__).resolve().parent.parent
# sys.path.insert(0, str(PROJECT_ROOT))

# # import load data module from project folder
# from project.load_data import get_data
# from project import descriptive_summary as ds
# FILENAME = PROJECT_ROOT / "data" / "lung_cancer_dataset.csv"


class TestLoadData(unittest.TestCase):

    def test_load_data(self):
        """Checks that the data is loaded correctly by confirming data shape."""
        df = l.get_data("data/lung_cancer_dataset.csv")
        assert df.shape == (2000, 46)       # Expecting 2000 rows and 46 columns 

    def test_category_count(self): 
        df = pd.DataFrame({
            'Column1': ['a', 'b', 'c', 'a']
        })

        test_summary = ds.DescriptiveSummary(df)
        actual = test_summary.get_category_count('Column1', df)
        expected = pd.Series(
            {'a': 2, 'b': 1, 'c': 1}, 
            name = 'count'
        ).rename_axis('Column1')

        pd.testing.assert_series_equal(expected, actual)

    def test_calc_mean(self):
        df = pd.DataFrame({
            'Column1': [1, 2, 3, 4]
        })

        test_summary = ds.DescriptiveSummary(df)
        actual = test_summary.calc_mean('Column1', df)
        expected = 2.5

        self.assertEqual(expected, actual)

    def test_calc_median(self):
        df = pd.DataFrame({
            'Column1': [1, 2, 3, 4]
        })

        test_summary = ds.DescriptiveSummary(df)
        actual = test_summary.calc_median('Column1', df)
        expected = 2.5

        self.assertEqual(expected, actual)
    
    def test_calc_mode(self):
        df = pd.DataFrame({
            'Column1': [1, 2, 2, 3, 4]
        })

        test_summary = ds.DescriptiveSummary(df)
        actual = test_summary.calc_mode('Column1', df)
        expected = 2

        self.assertEqual(expected, actual)

# if __name__ == "__main__": 
#     t = TestLoadData()

#     # Create a list of tests (functions) so it is easy to add more test functions later.
#     # If you added more tests, you need to add them to this list. 
#     tests = [
#         t.test_load_data, 
#         t.test_category_count,
#         t.test_calc_mean,
#         t.test_calc_median,
#         t.test_calc_mode
#         ]

#     # Run all tests in your tests list.
#     for test in tests:
#         try:
#             # Run the test and it should print PASSED.
#             test()
#             print(f"{test.__name__}: PASSED") 

#         except AssertionError:
#             # If the assert fails, it should show FAILED.
#             print(f"{test.__name__}: FAILED")

#         finally:
#             # Indicate the test was run successfully. 
#             print("Test completed.\n")

if __name__ == "__main__": 
    unittest.main()
