# 📂 tests/test_filter.py - Pruebas de filtrado de datos

import unittest
import pandas as pd
from src.filter_by_date import filter_by_date

class TestFilterData(unittest.TestCase):
    def test_filter(self):
        df = pd.DataFrame({"fecha": ["2024-05-01", "2024-06-01"], "valor": [100, 200]})
        df_filtered = filter_by_date(df, "2024-05-01")
        self.assertEqual(len(df_filtered), 1)

if __name__ == "__main__":
    unittest.main()