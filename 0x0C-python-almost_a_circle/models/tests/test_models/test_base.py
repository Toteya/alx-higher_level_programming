#!/usr/bin/python3
""" Unittest for Base class
"""
import unittest
import json
from models.base import Base


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

    def test_to_json_string(self):
        """ Test the to_json_string static method which returns a JSON
        string representation of the list of dictionaries given
        """
        list_dicts = [{'id': 1, 'size': 4}, {'x': 2, 'y': 4}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual('[{"id": 1, "size": 4}, {"x": 2, "y": 4}]', json_str)
