"""Module with a class for tests"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Class with method tests"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_valid_attributes(self):
        r1 = Rectangle(5, 10, 0, 0)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rectangle_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_six_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1)

    def test_invalid_width_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("invalid", 10, 1, 1, 1)

    def test_invalid_width_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 10, 1, 1, 1)

    def test_invalid_height_type(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(5, "invalid", 1, 1, 1)

    def test_invalid_height_value(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(5, 0, 1, 1, 1)

    def test_invalid_x_type(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(5, 10, "invalid", 1, 1)

    def test_invalid_x_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(5, 10, -1, 1, 1)

    def test_invalid_y_type(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(5, 10, 1, "invalid", 1)

    def test_invalid_y_type(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1 = Rectangle(5, 10, 1, -1, 1)

    def test_rectangle_area(self):
        r1 = Rectangle(2, 5)
        self.assertEqual(r1.area(), 10)

    def test_rectangle_display(self):
        r1 = Rectangle(3, 2, 2, 1)

        expected_output = "\n  ###\n  ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_rectangle_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_kwargs(self):
        r1 = Rectangle(1, 2, 3, 4)
        r1.update(x=2, y=2, width=2, height=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/2 - 2/2")

        r1.update(1, 3, 4, width=2, height=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/2 - 3/4")

    def test_rectangle_dictionary(self):
        r1 = Rectangle(1, 2, 3, 4)
        r1_dict = r1.to_dictionary()
        self.assertEqual(
                str(r1_dict),
                "{'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4}"
        )

        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        self.assertEqual(str(r2), "[Rectangle] (1) 3/4 - 1/2")


if __name__ == "__main__":
    unittest.main()
