import unittest
import pandas as pd
from src import data_cleaning

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Stone_Category': ['CaP', 'Brushite', 'CaOx', 'CaP'],
            'pH_category': ['High', 'Low', 'High', 'Low'],
            'Ca24': [100, 150, 120, 130],
            'SSCaP': [30, 35, 32, 31],
            'Ca24kg': [0.8, 0.9, 0.85, 0.87],
            'Ca24Cr24': [0.75, 0.8, 0.78, 0.76],
            'Cit24': [500, 520, 510, 515],
            'Serum_Ca': [9.5, 9.7, 9.6, 9.55],
            'Age': [45, 50, 38, 42],
            'BMI': [25, 28, 24, 26]
        })

    def test_clean_litholink_main(self):
        cleaned_df = data_cleaning.clean_litholink_main(self.df)
        self.assertEqual(set(cleaned_df.columns), 
                         {'Stone_Category', 'pH_category', 'Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca', 'Age', 'BMI'})
        self.assertFalse(cleaned_df.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
