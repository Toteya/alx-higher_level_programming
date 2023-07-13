#!/usr/bin/python3
""" Unittest for rectangle module
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """ Tests the Rectangle class and its
    methods
    """

    def test_Rectangle(self):
        """ Tests the Rectangle instantiation
        """
        rect1 = Rectangle(2, 4)
        self.assertTrue(isinstance(rect1, Rectangle))
        self.assertTrue(isinstance(rect1, Base))
        self.assertTrue(issubclass(rect1.__class__, Base))
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect1.width, 2)
        self.assertEqual(rect1.height, 4)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

        rect2 = Rectangle(5, 5, 2, 3)
        self.assertEqual(rect2.id, 2)
        self.assertEqual(rect2.width, 5)
        self.assertEqual(rect2.height, 5)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2.y, 3)

        rect3 = Rectangle(3, 4, id=98)
        self.assertEqual(rect3.id, 98)

        with self.assertRaises(TypeError):
            Rectangle()

    def test_width(self):
        """ Tests getter and setter for Rectangle width
        """
        rect = Rectangle(2, 3)
        self.assertEqual(rect.width, 2)
        rect.width = 1
        self.assertEqual(rect.width, 1)

    def test_height(self):
        """ Tests getter and setter for Rectangle height
        """
        rect = Rectangle(2, 3)
        self.assertEqual(rect.height, 3)
        rect.height = 4
        self.assertEqual(rect.height, 4)

    def test_x(self):
        """ Tests getter and setter for Rectangle private attriibute x
        """
        rect = Rectangle(2, 3, 1, 1)
        self.assertEqual(rect.x, 1)
        rect.x = 0
        self.assertEqual(rect.x, 0)

    def test_y(self):
        """ Tests getter and setter for Rectangle private attriibute y
        """
        rect = Rectangle(2, 3, 1, 1)
        self.assertEqual(rect.y, 1)
        rect.y = 5
        self.assertEqual(rect.y, 5)
