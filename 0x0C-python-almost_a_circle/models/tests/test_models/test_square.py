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

    def test_Square(self):
        """ Tests the instantiation of a Square object
        """
        square = Square(4)
        square_str = "[Square] (1) 0/0 - 4"
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

        square = Square(5, 2, 1)
        square_str = f"[Square] ({square.id}) 2/1 - 5"
        self.assertEqual(square.__str__(), square_str)

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
