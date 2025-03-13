# 📂 tests/test_transform.py - Pruebas de transformación de datos en Databricks

import unittest
from src.transform_data_databricks import transform_data

class TestTransformData(unittest.TestCase):
    def test_transform(self):
        try:
            transform_data()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()