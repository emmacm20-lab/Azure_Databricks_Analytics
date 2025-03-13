# 📂 tests/test_analytics.py - Pruebas de análisis en PySpark

import unittest
from src.analytics_pyspark import run_analytics

class TestAnalytics(unittest.TestCase):
    def test_analytics(self):
        try:
            run_analytics()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()