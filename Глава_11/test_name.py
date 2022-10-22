import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formattedName = get_formatted_name('janis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')

    def test_first_middle_last_name(self):
        formattedName = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formattedName, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
