# _*_ coding: utf-8 _*_

"""This is a Simple Test Module"""

from unittest import TestCase
from ci_example.calculator import Calculator

class CiExampleTests(TestCase):
    """Simple CI Example Test Class"""

    def setUp(self):
        TestCase.setUp(self)

    @staticmethod
    def test_number_is_even():
        """Simple Test for even numbers"""
        calc = Calculator.number_is_even()
        assert calc(2) == 0

    def test_adder(self):
        """Simple test for sum numbers"""
        calc = Calculator.adder()
        result = calc(2, 2)
        self.assertEqual(4, result)
