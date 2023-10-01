#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 4, 5, -3, 2]), 5)
        self.assertEqual(max_integer([1, 4, 8.8, -3, 2]), 8.8)
        self.assertEqual(max_integer([]), None)

    def test_type(self):
        self.assertRaises(TypeError, max_integer, [1, "hello", 2, 3])
