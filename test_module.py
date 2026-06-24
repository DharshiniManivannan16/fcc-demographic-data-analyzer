import unittest
import demographic_data_analyzer
import pandas as pd

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data = False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [19560, 8150, 3260, 1630]
        self.assertCountEqual(actual, expected, msg="Expected different values for race count.")

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 38.7
        self.assertAlmostEqual(actual, expected, places=1, msg="Expected different value for average age of men.")

    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 30.0
        self.assertAlmostEqual(actual, expected, places=1, msg="Expected different value for percentage bachelors.")

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 44.4
        self.assertAlmostEqual(actual, expected, places=1, msg="Expected different value for higher education rich.")

    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 27.3
        self.assertAlmostEqual(actual, expected, places=1, msg="Expected different value for lower education rich.")

    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 13
        self.assertEqual(actual, expected, msg="Expected different value for minimum work hours.")

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 0.0
        self.assertAlmostEqual(actual, expected, places=1, msg="Expected different value for rich percentage.")

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'India'
        self.assertEqual(actual, expected, msg="Expected different value for highest earning country.")

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 100.0
        self.assertAlmostEqual(actual, expected, places=1, msg="Expected different value for highest earning country percentage.")

    def test_top_IN_occupation(self):
        actual = self.data['top_IN_occupation']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected, msg="Expected different value for top India occupation.")

if __name__ == "__main__":
    unittest.main()
