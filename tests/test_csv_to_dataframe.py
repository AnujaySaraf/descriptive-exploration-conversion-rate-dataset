from unittest import TestCase
import pandas as pd


filepath = "./data/conversion_data.csv"


class TestCsv_to_dataframe(TestCase):
    def test_csv_to_dataframe(self):
        from build import csv_to_dataframe
        res = csv_to_dataframe(filepath)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_dtype_category(self):
        from build import csv_to_dataframe, dtype_category
        res = csv_to_dataframe(filepath)
        res_new = dtype_category(res, ["country", "new_user", "source", "converted"])
        self.assertTrue(isinstance(res_new, pd.DataFrame))

    def test_categorical_variable_count(self):
        from build import csv_to_dataframe, categorical_variable_count
        res = csv_to_dataframe(filepath)
        res_new = categorical_variable_count(res)
        self.assertEqual(4, res_new)

    def test_var_ckeck(self):
        from build import csv_to_dataframe, var_ckeck
        res = csv_to_dataframe(filepath)
        res_new = var_ckeck(res, 5)
        self.assertEqual([], res_new)

    def test_logistic_regression_model(self):
        from build import csv_to_dataframe, logistic_regression_model
        res = csv_to_dataframe(filepath)
        res_new = logistic_regression_model(res, "converted", ['country_China', 'country_Germany', 'country_UK', 'country_US',
       'source_Ads', 'source_Direct', 'source_Seo', 'age', 'new_user',
       'total_pages_visited', 'Constant Term', 'age^2',
       'age x total_pages_visited', 'total_pages_visited^2', 'age^3',
       'age^2 x total_pages_visited', 'age x total_pages_visited^2',
       'total_pages_visited^3'])
        self.assertAlmostEqual(res_new, 98.282099936748892, places=3)