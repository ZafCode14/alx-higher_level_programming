"""Module with a unittest for Base"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    """Class of methods for unittest"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(5)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 5)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(
                str(json_dictionary),
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        )
        json_dictionary = Base.to_json_string([])
        self.assertEqual(str(json_dictionary), '[]')

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(str(json_dictionary), '[]')

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(4, 2)

        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                    str(f.read()),
                    '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
                    '{"id": 2, "width": 4, "height": 2, "x": 0, "y": 0}]'
            )

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(str(f.read()), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(str(f.read()), '[]')

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_output, list)
        self.assertEqual(
                str(list_output),
                "[{'id': 89, 'width': 10, 'height': 4}, "
                "{'id': 7, 'width': 1, 'height': 7}]"
        )

        list_output = Rectangle.from_json_string(None)
        self.assertEqual(str(list_output), "[]")

        list_output = Rectangle.from_json_string("[]")
        self.assertEqual(str(list_output), "[]")

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")

    def test_load_and_save_form_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()

        self.assertEqual(str(output[0]), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(output[1]), "[Rectangle] (2) 0/0 - 2/4")

    def test_load_and_save_to_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()

        self.assertEqual(str(output[0]), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(output[1]), "[Rectangle] (2) 0/0 - 2/4")


if __name__ == "__main__":
    unittest.main()
