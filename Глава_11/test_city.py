import unittest
from city_functions import get_country_city


class NameTestWorld(unittest.TestCase):

    def test_country_city(self):
        worldName = get_country_city('россия', 'москва')
        self.assertEqual(worldName, 'Россия Москва')

    def test_country_citi_population(self):
        worldName = get_country_city('santiago', 'chile', 50000)
        self.assertEqual(worldName, 'Santiago Chile 50000')


if __name__ == '__main__':
    unittest.main()
