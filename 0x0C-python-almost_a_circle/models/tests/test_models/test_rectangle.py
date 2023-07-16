#!/usr/bin/python3
""" Unittest for rectangle module
"""
from unittest import TestCase
from unittest.mock import patch, mock_open
from io import StringIO
import json
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(TestCase):
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

        with self.assertRaises(TypeError):
            rect.width = None
        with self.assertRaises(TypeError):
            rect.width = '2'
        with self.assertRaises(TypeError):
            rect.width = [2]
        with self.assertRaises(TypeError):
            rect.width = (2,)
        with self.assertRaises(TypeError):
            rect.width = {2, 3}
        with self.assertRaises(TypeError):
            rect.width = (2.0)
        with self.assertRaises(ValueError):
            rect.width = (0)
        with self.assertRaises(ValueError):
            rect.width = (-1)

    def test_height(self):
        """ Tests getter and setter for Rectangle height
        """
        rect = Rectangle(2, 3)
        self.assertEqual(rect.height, 3)
        rect.height = 4
        self.assertEqual(rect.height, 4)

        with self.assertRaises(TypeError):
            rect.height = None
        with self.assertRaises(TypeError):
            rect.height = '2'
        with self.assertRaises(TypeError):
            rect.height = [2]
        with self.assertRaises(TypeError):
            rect.height = (2,)
        with self.assertRaises(TypeError):
            rect.height = {2, 3}
        with self.assertRaises(TypeError):
            rect.height = (2.0)
        with self.assertRaises(ValueError):
            rect.height = (0)
        with self.assertRaises(ValueError):
            rect.height = (-1)

    def test_x(self):
        """ Tests getter and setter for Rectangle private attriibute x
        """
        rect = Rectangle(2, 3, 1, 1)
        self.assertEqual(rect.x, 1)
        rect.x = 0
        self.assertEqual(rect.x, 0)

        with self.assertRaises(TypeError):
            rect.x = None
        with self.assertRaises(TypeError):
            rect.x = '2'
        with self.assertRaises(TypeError):
            rect.x = [2]
        with self.assertRaises(TypeError):
            rect.x = (2,)
        with self.assertRaises(TypeError):
            rect.x = {2, 3}
        with self.assertRaises(TypeError):
            rect.x = (2.0)
        with self.assertRaises(ValueError):
            rect.x = (-1)

    def test_y(self):
        """ Tests getter and setter for Rectangle private attriibute y
        """
        rect = Rectangle(2, 3, 1, 1)
        self.assertEqual(rect.y, 1)
        rect.y = 5
        self.assertEqual(rect.y, 5)

        with self.assertRaises(TypeError):
            rect.y = None
        with self.assertRaises(TypeError):
            rect.y = '2'
        with self.assertRaises(TypeError):
            rect.y = [2]
        with self.assertRaises(TypeError):
            rect.y = (2,)
        with self.assertRaises(TypeError):
            rect.y = {2, 3}
        with self.assertRaises(TypeError):
            rect.y = (2.0)
        with self.assertRaises(ValueError):
            rect.y = (-1)

    def test_validate_int(self):
        """ Tests the validate_int method
        """
        rect = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            rect.validate_int()
        with self.assertRaises(TypeError):
            rect.validate_int("x")
        with self.assertRaises(TypeError):
            rect.validate_int("x", '3')
        with self.assertRaises(TypeError):
            rect.validate_int("x", [3])
        with self.assertRaises(TypeError):
            rect.validate_int("x", (3,))
        with self.assertRaises(TypeError):
            rect.validate_int("x", {3})
        with self.assertRaises(TypeError):
            rect.validate_int("x", 3.0)
        with self.assertRaises(TypeError):
            rect.validate_int("x", None)

    def test_validate_ge_zero(self):
        """ Tests the validate_ge_zero method
        """
        rect = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            rect.validate_ge_zero()
        with self.assertRaises(TypeError):
            rect.validate_ge_zero("y")
        with self.assertRaises(ValueError):
            rect.validate_ge_zero("y", -5)

    def test_validate_gt_zero(self):
        """ Tests the validate_gt_zero method
        """
        rect = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            rect.validate_gt_zero()
        with self.assertRaises(TypeError):
            rect.validate_gt_zero("width")
        with self.assertRaises(ValueError):
            rect.validate_gt_zero("width", 0)
        with self.assertRaises(ValueError):
            rect.validate_gt_zero("width", -5)

    def test_area(self):
        """ Tests the area() method that returns the area
        of a Rectangle instance
        """
        rect = Rectangle(2, 4, 0, 0)
        self.assertEqual(rect.area(), 8)

        rect.width = 4
        self.assertEqual(rect.area(), 16)

    def test_display(self):
        """ Tests the display() method that prints a Rectangle to stdout
        """
        rect1 = Rectangle(1, 1)
        rect1_exp_out = "#\n"

        rect2 = Rectangle(2, 4)
        rect2_exp_out = "\
##\n\
##\n\
##\n\
##\n"

        rect3 = Rectangle(3, 4, 2)
        rect3_exp_out = "\
  ###\n\
  ###\n\
  ###\n\
  ###\n"

        rect4 = Rectangle(3, 3, 1, 2)
        rect4_exp_out = "\
\n\
\n\
 ###\n\
 ###\n\
 ###\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rect1.display()
            self.assertEqual(fake_out.getvalue(), rect1_exp_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rect2.display()
            self.assertEqual(fake_out.getvalue(), rect2_exp_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rect3.display()
            self.assertEqual(fake_out.getvalue(), rect3_exp_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rect4.display()
            self.assertEqual(fake_out.getvalue(), rect4_exp_out)

    def test_str(self):
        """ Tests the Rectangle's __str__ method
        """
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect2 = Rectangle(4, 4, 2)

        rect1_out = "[Rectangle] (5) 3/4 - 1/2"
        rect2_out = "[Rectangle] ({}) 2/0 - 4/4".format(rect2.id)

        self.assertEqual(rect1.__str__(), rect1_out)
        # self.assertEqual(rect2.__str__(), rect2_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(rect1)
            self.assertEqual(fake_out.getvalue().strip(), rect1_out)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(rect2)
            self.assertEqual(fake_out.getvalue().strip(), rect2_out)

    def test_update(self):
        """ Tests the update method that updates the attributes of a
        Rectangle instance
        """
        rect = Rectangle(3, 3, id=75)
        self.assertEqual(rect.__str__(), "[Rectangle] (75) 0/0 - 3/3")
        rect.update(83, 4, 4, 1, 2)
        self.assertEqual(rect.__str__(), "[Rectangle] (83) 1/2 - 4/4")
        rect.update(90)
        self.assertEqual(rect.__str__(), "[Rectangle] (90) 1/2 - 4/4")
        rect.update(90, 2)
        self.assertEqual(rect.__str__(), "[Rectangle] (90) 1/2 - 2/4")
        rect.update(90, 2, 3)
        self.assertEqual(rect.__str__(), "[Rectangle] (90) 1/2 - 2/3")
        rect.update(90, 2, 3, 0)
        self.assertEqual(rect.__str__(), "[Rectangle] (90) 0/2 - 2/3")
        rect.update(90, 2, 3, 0, 1)
        self.assertEqual(rect.__str__(), "[Rectangle] (90) 0/1 - 2/3")
        rect.update(None)
        self.assertEqual(rect.__str__(), "[Rectangle] (None) 0/1 - 2/3")
        rect.update('A')
        self.assertEqual(rect.__str__(), "[Rectangle] (A) 0/1 - 2/3")
        rect.update(90, id=88)
        self.assertEqual(rect.__str__(), "[Rectangle] (90) 0/1 - 2/3")
        rect.update(90, 7, 5, id=88, width=3, height=2)
        self.assertEqual(rect.__str__(), "[Rectangle] (90) 0/1 - 7/5")
        rect.update(id=88, width=3, height=2)
        self.assertEqual(rect.__str__(), "[Rectangle] (88) 0/1 - 3/2")
        rect.update(id=88, width=3, height=2, x=3, y=0)
        self.assertEqual(rect.__str__(), "[Rectangle] (88) 3/0 - 3/2")
        rect.update(x=2, y=2)
        self.assertEqual(rect.__str__(), "[Rectangle] (88) 2/2 - 3/2")
        with self.assertRaises(AttributeError):
            rect.update(name=88)

    def test_to_dictionary(self):
        """ Tests to_dictionary() method that returns a dictionary
        representation of the Rectangle
        """
        rect = Rectangle(8, 6, 2, 2, 54)
        rect_dict = {'x': 2, 'y': 2, 'id': 54, 'height': 6, 'width': 8}
        self.assertEqual(rect.to_dictionary(), rect_dict)

        rect = Rectangle(5, 4)
        rect_dict = {'x': 0, 'y': 0, 'id': rect.id, 'height': 4, 'width': 5}
        self.assertEqual(rect.to_dictionary(), rect_dict)

    def test_to_json_string(self):
        """ Tests the static method that returns a JSON string representation
        of a list of dictionaries representing rectangles
        """
        rect = Rectangle(4, 3, 1, 2, id=77)
        json_str = Rectangle.to_json_string([rect.to_dictionary()])
        exp_out = '[{"id": 77, "width": 4, "height": 3, "x": 1, "y": 2}]'
        self.assertTrue(isinstance(json_str, str))
        self.assertEqual(exp_out, json_str)

        json_str = Rectangle.to_json_string([])
        self.assertEqual('[]', json_str)

        #json_str = Rectangle.to_json_string()
        #self.assertEqual('[]', json_str)

    def test_save_to_file(self):
        """ Tests the class method `save_to_file` which saves the JSON
        representation of a list of Rectangle instances to a file
        """
        r1 = Rectangle(4, 5, id=4)
        r2 = Rectangle(2, 6, 1, 1, id=6)
        list_objs = [r1, r2]
        exp_out = '[{"id": 4, "width": 4, "height": 5, "x": 0, "y": 0}, \
                {"id": 6, "width": 2, "height": 6, "x": 1, "y": 1}]'
        with patch('builtins.open', create=True) as fake_file:
            Rectangle.save_to_file(list_objs)
            fake_file.assert_called_once_with("Rectangle.json", mode="w", encoding="utf-8")
            # fake_file.return_value.write.assert_called_once_with(exp_out)

            
            # content = fake_file.return_value.read.return_value
            # self.assertEqual(content, exp_out)
    
        list_objs = []
        with patch('builtins.open', create=True) as fake_file:
            Rectangle.save_to_file(list_objs)
            fake_file.assert_called_once_with("Rectangle.json", mode="w", encoding="utf-8")
