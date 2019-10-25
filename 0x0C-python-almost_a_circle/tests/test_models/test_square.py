#!/usr/bin/python3
""" unit tests for rectangle """
import unittest
import pep8
from models.rectangle import Rectangle

Base = models.base.Base
Rectangle = models.rectangle.Rectangle
Square = models.square.Square


class TestSquare(unittest.TestCase):
    """ Class rectangle tests """
    def test_pep8(self):
        """ tests prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")
