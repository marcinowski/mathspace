"""
:created on: 2017-07-08

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from .converter import BaseConvertClass


class WrongNumberFormat(Exception):
    """"""


class DecryptCityNumber(BaseConvertClass):
    """
    Class for validating an input number and converting it into city name.
    """

    def parse(self):
        """
        Converts string representation of a number to decoded city name.
        :return: decrypted city name
        :rtype: str
        """
        list_of_chr = [self._clear_two_digits(self.value[i:i + 3]) for i in range(0, len(self.value), 3)]
        self.result = ''.join(map(lambda x: chr(int(x)), list_of_chr))
        return self.result

    @staticmethod
    def _clear_two_digits(x):
        if x.startswith('-') or x.startswith('0'):
            return x[1:]
        return x

    @staticmethod
    def _validate_input(value):
        if len(value) % 3:
            raise WrongNumberFormat('Wrong number format. Should contain 3n characters.')
        if not isinstance(value, str):
            raise WrongNumberFormat('Only string format is supported.')
        return value


if __name__ == '__main__':
    import sys
    number = sys.argv[1].strip()
    result = DecryptCityNumber(sys.argv[1]).parse()
    print('Number to decrypt: {}'.format(number))
    print('Result: {}'.format(result))
