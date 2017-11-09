import unittest
from name_func import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def  test_first_last_name(self):
        formatted_name = get_formatted_name("roman", "efimov")
        self.assertEqual(formatted_name, "Roman Efimov")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name("roman", "sergeevich", "efimov")
        self.assertEqual(formatted_name, "Roman Sergeevich Effimov")

unittest.main()
