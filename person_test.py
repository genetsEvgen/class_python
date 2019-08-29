import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_get_name(self):
        person1 = Person("Ivan")
        self.assertEqual(person1.name, "Ivan")

if __name__ == '__main__':
    unittest.main()


#https://pythonworld.ru/moduli/modul-unittest.html