# UNIT TESTS FOR TDD 
import unittest
import sys
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# import load data module from project folder
from project import load_data as l
from project import descriptive_summary as ds
FILENAME = PROJECT_ROOT / "data" / "lung_cancer_dataset.csv"


class TestLoadData(unittest.TestCase):

    def test_load_data(self):
        """Checks that the data is loaded correctly by confirming data shape."""
        df = l.get_data(FILENAME)
        assert df.shape == (2000, 46)       # Expecting 2000 rows and 46 columns 

    def test_load_from_db(self):
        """Checks that the data is loaded correctly by confirming data shape."""
        df = l.get_lung_cancer_data()
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

if __name__ == "__main__": 
    unittest.main()
