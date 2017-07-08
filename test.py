"""
:created on: 2017-07-08

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from unittest import TestCase

from simple import ConvertCityName, WrongNameFormat


class TestConvertCityName(TestCase):
    def test_capital_error_handling(self):
        with self.assertRaises(WrongNameFormat):
            ConvertCityName('TeSt')

    def test_empty_error_handling(self):
        with self.assertRaises(WrongNameFormat):
            ConvertCityName('')
        with self.assertRaises(WrongNameFormat):
            ConvertCityName(None)

    def test_number_error_handling(self):
        with self.assertRaises(WrongNameFormat):
            ConvertCityName(5)
#
# def test_converting(self):
#     c = ConvertCityName('')
    