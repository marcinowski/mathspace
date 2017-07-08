"""
:created on: 2017-07-08

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""

from unittest import TestCase

from converter import ConvertCityName, WrongNameFormat
from decryptor import DecryptCityNumber, WrongNumberFormat


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
        c = ConvertCityName('def').parse()
        result = str(ord('d')) + str(ord('e')) + str(ord('f'))  # 100101102
        self.assertEqual(c, result)

    def test_first_letter_parsing(self):
        """ First letter should be parsed to negative if less than 3 digits """
        c = ConvertCityName('ad').parse()
        self.assertEqual(c, '-97100')

    def test_abc_in_string(self):
        """ a, b & c as 2 digit numbers should be followed by 0 """
        c = ConvertCityName('eaebece').parse()
        self.assertEqual(c, '101097101098101099101')

    def test_space(self):
        """ Test for space handling """
        c = ConvertCityName('e e').parse()
        self.assertEqual(c, '101032101')


class TestDecryptWrongCityNumber(TestCase):
    def test_wrong_number(self):
        with self.assertRaises(WrongNumberFormat):
            DecryptCityNumber('12')

    def test_int_argument(self):
        with self.assertRaises(WrongNumberFormat):
            DecryptCityNumber(123)


class TestDecryptCityNumber(TestCase):
    def test_general_concept(self):
        """ Simple test for conceptual purpose """
        d = DecryptCityNumber('101'+'102').parse()
        result = chr(101) + chr(102)  # 'ef'
        self.assertEqual(d, result)
