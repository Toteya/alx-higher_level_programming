#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests max_integer function
    """

    def test_max_integer(self):
        """ Tests cases that should pass
        """
        result = max_integer([2, 6, 8, 4])
        self.assertEqual(result, 8)
        
        result = max_integer([10, 2, 6, 4])
        self.assertEqual(result, 10)

        result = max_integer([2, 6, 8, 12])
        self.assertEqual(result, 12)
        
        result = max_integer([2, 6, -8, 4])
        self.assertEqual(result, 6)

        result = max_integer([-2, 0, -8])
        self.assertEqual(result, 0)

        result = max_integer([3])
        self.assertEqual(result, 3)

        result = max_integer([])
        self.assertEqual(result, None)
