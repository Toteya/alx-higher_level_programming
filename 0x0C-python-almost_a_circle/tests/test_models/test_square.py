#!/usr/bin/python3
""" Unittest for square module
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(TestCase):
    """ Tests the Square class and its
    methods
    """

    def setUp(self):
        """ Sets up the initial conditions for each test
        case
        """
        Base._Base__nb_objects = 0

    def test_Square(self):
        """ Tests the instantiation of a Square object
        """
        square = Square(4)
        square_str = f"[Square] ({square.id}) 0/0 - 4"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(square)
            self.assertEqual(fake_out.getvalue().strip(), square_str)

        self.assertTrue(isinstance(square, Square))
        self.assertTrue(isinstance(square, Rectangle))
        self.assertTrue(isinstance(square, Base))
        self.assertTrue(issubclass(square.__class__, Rectangle))
        self.assertTrue(issubclass(square.__class__, Base))
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.size, square.width)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        square = Square(4, 1, id=98)
        square_str = f"[Square] ({square.id}) 1/0 - 4"
        self.assertEqual(square.__str__(), square_str)

        square1 = Square(5, 2, 1)
        square1_str = f"[Square] (2) 2/1 - 5"
        self.assertEqual(square1.__str__(), square1_str)

        square = Square(5, 2, 1, 56)
        self.assertEqual(square.__str__(), "[Square] (56) 2/1 - 5")

        with self.assertRaises(TypeError):
            square1 = Square()

    def test_size(self):
        """ Tests the getter and setter methods for Square size
        """
        sq = Square(5, id=76)

        self.assertEqual(sq.size, 5)
        sq.size = 1
        self.assertEqual(sq.size, 1)

        with self.assertRaises(TypeError):
            sq.size = None
        with self.assertRaises(TypeError):
            sq.size = '2'
        with self.assertRaises(TypeError):
            sq.size = [2]
        with self.assertRaises(TypeError):
            sq.size = (2,)
        with self.assertRaises(TypeError):
            sq.size = {2, 3}
        with self.assertRaises(TypeError):
            sq.size = (2.0)
        with self.assertRaises(ValueError):
            sq.size = (0)
        with self.assertRaises(ValueError):
            sq.size = (-1)

    def test_area(self):
        """ Tests the area() method that returns the area
        of a Square instance
        """
        rect = Rectangle(2, 4, 0, 0)
        self.assertEqual(rect.area(), 8)

        rect.width = 4
        self.assertEqual(rect.area(), 16)

    def test_display(self):
        """ Tests the display() method that prints a Square to stdout
        """
        sq1 = Square(1)
        sq1_exp_out = "#\n"

        sq2 = Square(4)
        sq2_exp_out = "\
####\n\
####\n\
####\n\
####\n"

        sq3 = Square(3, 3)
        sq3_exp_out = "\
   ###\n\
   ###\n\
   ###\n"

        sq4 = Square(2, 2, 2)
        sq4_exp_out = "\
\n\
\n\
  ##\n\
  ##\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            sq1.display()
            self.assertEqual(fake_out.getvalue(), sq1_exp_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            sq2.display()
            self.assertEqual(fake_out.getvalue(), sq2_exp_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            sq3.display()
            self.assertEqual(fake_out.getvalue(), sq3_exp_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            sq4.display()
            self.assertEqual(fake_out.getvalue(), sq4_exp_out)

    def test_str(self):
        """ Tests the Square's __str__ representation
        """
        sq1 = Square(2, 3, 4, 31)
        sq2 = Square(4, 2)

        sq1_out = "[Square] (31) 3/4 - 2"
        sq2_out = "[Square] ({}) 2/0 - 4".format(sq2.id)

        self.assertEqual(sq1.__str__(), sq1_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(sq1)
            self.assertEqual(fake_out.getvalue().strip(), sq1_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(sq2)
            self.assertEqual(fake_out.getvalue().strip(), sq2_out)

    def test_update(self):
        """ Tests the update method that updates the attributes of a
        Square instance
        """
        sq = Square(3, id=75)
        self.assertEqual(sq.__str__(), "[Square] (75) 0/0 - 3")
        sq.update(83, 4, 1, 2)
        self.assertEqual(sq.__str__(), "[Square] (83) 1/2 - 4")
        sq.update(90)
        self.assertEqual(sq.__str__(), "[Square] (90) 1/2 - 4")
        sq.update(90, 2)
        self.assertEqual(sq.__str__(), "[Square] (90) 1/2 - 2")
        sq.update(90, 2, 3)
        self.assertEqual(sq.__str__(), "[Square] (90) 3/2 - 2")
        sq.update(90, 2, 3, 0)
        self.assertEqual(sq.__str__(), "[Square] (90) 3/0 - 2")
        sq.update(None)
        self.assertEqual(sq.__str__(), "[Square] (None) 3/0 - 2")
        sq.update('A')
        self.assertEqual(sq.__str__(), "[Square] (A) 3/0 - 2")
        sq.update(90, id=88)
        self.assertEqual(sq.__str__(), "[Square] (90) 3/0 - 2")
        sq.update(90, 7, 5, id=88, size=3)
        self.assertEqual(sq.__str__(), "[Square] (90) 5/0 - 7")
        sq.update(id=88, size=2)
        self.assertEqual(sq.__str__(), "[Square] (88) 5/0 - 2")
        sq.update(id=88, size=4, x=1, y=1)
        self.assertEqual(sq.__str__(), "[Square] (88) 1/1 - 4")
        sq.update(x=2, y=2)
        self.assertEqual(sq.__str__(), "[Square] (88) 2/2 - 4")
        with self.assertRaises(AttributeError):
            sq.update(id=8, name=88)

    def test_to_dictionary(self):
        """ Tests to_dictionary() method that returns a dictionary
        representation of the Square
        """
        sq = Square(8, 2, 3, 43)
        sq_dict = {'id': 43, 'x': 2, 'size': 8, 'y': 3}
        self.assertEqual(sq.to_dictionary(), sq_dict)

        sq = Square(5, 4)
        sq_dict = {'id': sq.id, 'x': 4, 'size': 5, 'y': 0}
        self.assertEqual(sq.to_dictionary(), sq_dict)

    def test_to_json_string(self):
        """ Tests the static method that returns a JSON string representation
        of a list of dictionaries representing Square instances
        """
        sq = Square(3, id=61)
        json_str = Square.to_json_string([sq.to_dictionary()])
        exp_out = '[{"id": 61, "x": 0, "y": 0, "size": 3}]'
        self.assertTrue(isinstance(json_str, str))
        self.assertEqual(exp_out, json_str)

    def test_from_json_string(self):
        """ Test the method that returns a list of dictionaries
        from JSON string representation
        """
        sq = Square(4)
        json_str = Square.to_json_string([sq.to_dictionary()])
        self.assertTrue(isinstance(json_str, str))

        json_list = Square.from_json_string(json_str)
        self.assertTrue(isinstance(json_list, list))
        self.assertTrue(isinstance(json_list[0], dict))
        self.assertEqual(json_list, [{'id': 1, 'size': 4,
                                     'x': 0, 'y': 0}])

        json_list = Square.from_json_string("")
        self.assertTrue(isinstance(json_list, list))
        self.assertEqual(json_list, [])

        json_list = Square.from_json_string(None)
        self.assertTrue(isinstance(json_list, list))
        self.assertEqual(json_list, [])

        with self.assertRaises(TypeError):
            json_list = Square.from_json_string()

    def test_create(self):
        """ Tests the class method create() that create and returns
        a new Square instance
        """
        sq1 = Square(6, 1, 1, 37)
        self.assertTrue(isinstance(sq1, Square))
        self.assertTrue(isinstance(sq1, Rectangle))
        sq2 = Square.create(**sq1.to_dictionary())
        self.assertTrue(isinstance(sq2, Square))
        self.assertEqual(37, sq2.id)
        self.assertEqual(sq2.to_dictionary(), {'id': 37, 'x': 1, 'y': 1,
                                               'size': 6})
        self.assertFalse(sq1 is sq2)
        self.assertFalse(sq1 == sq2)
        self.assertTrue(sq1.to_dictionary() == sq2.to_dictionary())

        with self.assertRaises(TypeError):
            Square.create(4, id=3, x=1, y=0)

        sq = Square.create(id=3, x=0, y=0)
        self.assertEqual(sq.to_dictionary(), {'id': 3, 'x': 0, 'y': 0,
                                              'size': 1})
