# 📂 tests/test_ingest.py - Pruebas de carga de datos en Azure Data Lake

import unittest
from src.ingest_csv_json_parquet import upload_file

class TestIngestData(unittest.TestCase):
    def test_upload(self):
        try:
            upload_file("data-lake-container", "./data/dummy.csv", "dummy.csv")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()