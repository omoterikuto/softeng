import unittest
from person import Person


class PersonTest(unittest.TestCase):
    def test_office_telephone_number(self):
        office_number = "001"
        telephone_number = "11122223333"
        p = Person("name", "company", office_number, telephone_number)
        self.assertEqual(p.office_telephone_number, office_number+"-"+telephone_number)