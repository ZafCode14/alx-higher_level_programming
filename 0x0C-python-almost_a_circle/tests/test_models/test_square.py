from models.square import Square
from models.base import Base
from io import StringIO
import sys
import unittest

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(size=7, id=89, y=1, x=12)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_square_display(self):
        s1 = Square(3, 1, 3)

        expected_output = "\n\n\n ###\n ###\n ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        s1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_square_dictionary(self):
        s1 = Square(1, 2, 3, 4)
        s1_dict = s1.to_dictionary()
        self.assertEqual(str(s1_dict), "{'id': 4, 'size': 1, 'x': 2, 'y': 3}")

        s2 = Square(1)
        s2.update(**s1_dict)
        self.assertEqual(str(s2), "[Square] (4) 2/3 - 1")

if __name__ == "__main__":
    unittest.main()
