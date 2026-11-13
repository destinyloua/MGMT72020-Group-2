# UNIT TESTS FOR TDD 
import unittest
import pandas as pd
from project import load_data as l
from project import descriptive_summary as ds 

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

if __name__ == "__main__": 
    unittest.main()
