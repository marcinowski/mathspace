"""
:created on: 2017-07-08

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from unittest import TestCase

from simple import ConvertCityName, WrongNameFormat


class TestConvertWrongCityName(TestCase):
    def test_capital_error_handling(self):
        """ Should fail on capitals - accepts only lower case """
        with self.assertRaises(WrongNameFormat):
            ConvertCityName('teSt')

    def test_empty_error_handling(self):
        """ Should fail on empty values """
        with self.assertRaises(WrongNameFormat):
            ConvertCityName('')
        with self.assertRaises(WrongNameFormat):
            ConvertCityName(None)

    def test_number_error_handling(self):
        """ Should fail on non string input """
        with self.assertRaises(WrongNameFormat):
            ConvertCityName(5)


class TestConvertCityName(TestCase):
    def test_general_concept(self):
        """ Simple test for conceptual purpose """
        c = ConvertCityName('def').convert()
        result = str(ord('d')) + str(ord('e')) + str(ord('f'))  # 100101102
        self.assertEqual(c, result)

    def test_first_letter_convertion(self):
        """ First letter should be converted to negative if less than 3 digits """
        c = ConvertCityName('ad').convert()
        self.assertEqual(c, '-97100')

    def test_abc_in_string(self):
        """ a, b & c as 2 digit numbers should be followed by 0 """
        c = ConvertCityName('eaebece').convert()
        self.assertEqual(c, '101097101098101099101')
