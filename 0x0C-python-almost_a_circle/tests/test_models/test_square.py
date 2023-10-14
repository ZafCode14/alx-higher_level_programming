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

    def test_valid_attributes(self):
        s1 = Square(10, 0, 0)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_square_six_args(self):
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1, 1)

    def test_invalid_size_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square("invalid", 1, 1, 1)

    def test_invalid_size_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(0, 1, 1, 1)

    def test_invalid_x_type(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(10, "invalid", 1, 1)

    def test_invalid_x_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1 = Square(10, -1, 1, 1)

    def test_invalid_y_type(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(10, 1, "invalid", 1)

    def test_invalid_y_type(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1 = Square(10, 1, -1, 1)

    def test_square_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_square_str(self):
        s1 = Square(6, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 6")

        s2 = Square(5, 1)
        self.assertEqual(str(s2), "[Square] (1) 1/0 - 5")

    def test_square_update(self):
        s1 = Square(10, 10, 10)
        s1.update(89, 3, 4, 5)
        self.assertEqual(str(s1), "[Square] (89) 4/5 - 3")

    def test_square_kwargs(self):
        s1 = Square(1, 2, 3)
        s1.update(x=2, y=2, size=2)
        self.assertEqual(str(s1), "[Square] (1) 2/2 - 2")

        s1.update(1, 3, size=5)
        self.assertEqual(str(s1), "[Square] (1) 2/2 - 3")

    def test_square_dictionary(self):
        s1 = Square(2, 3, 4)
        s1_dict = s1.to_dictionary()
        self.assertEqual(str(s1_dict), "{'id': 1, 'size': 2, 'x': 3, 'y': 4}")

        s2 = Square(1)
        s2.update(**s1_dict)
        self.assertEqual(str(s2), "[Rectangle] (1) 3/4 - 2")


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
