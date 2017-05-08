# _*_ coding: utf-8 _*_

"""This module is a simple calculator"""

class Calculator(object):
    """Simple Calculator class"""

    @staticmethod
    def number_is_even():
        """Return if number is even"""
        return lambda number: number%2

    @staticmethod
    def adder():
        """Return sum of two numbers"""
        return lambda number1, number2: number1+number2
