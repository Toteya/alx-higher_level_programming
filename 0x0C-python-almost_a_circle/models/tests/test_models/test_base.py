#!/usr/bin/python3
""" Unittest for Base class
"""
import unittest
from base import Base


class TestBase(unittest.TestCase):
    """ Tests the Base class
    """

    def test_Base(self):
        """ tests the Base class and instance methods
        """
        b0 = Base()
        self.assertEqual(b0.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b2 = Base(63)
        self.assertEqual(b2.id, 63)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        self.assertTrue(isinstance(b3, Base))
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
