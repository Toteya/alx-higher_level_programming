#!/usr/bin/python3
""" Unittest for Base class
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

        json_str = Base.to_json_string([])
        self.assertEqual('[]', json_str)
        self.assertTrue(isinstance(json_str, str))

    def test_create(self):
        """ Tests the class method create() that create and returns
        a new instance of the subclasses of Base
        """
        r1 = Rectangle(4, 6, 1, 1, 13)
        self.assertTrue(isinstance(r1, Rectangle))
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertTrue(isinstance(r2, Rectangle))
        self.assertEqual(13, r2.id)
        self.assertEqual(r2.to_dictionary(), {'id': 13, 'x': 1, 'y': 1,
                                              'width': 4, 'height': 6})
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        self.assertTrue(r1.to_dictionary() == r2.to_dictionary())

        with self.assertRaises(TypeError):
            Rectangle.create(2, 3, id=3, x=1, y=0)
