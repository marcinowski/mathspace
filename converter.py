"""
:created on: 2017-07-08

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""


class WrongNameFormat(Exception):
    """"""


class ConvertCityName(object):
    """
    Class for validating an input name and converting it into unique number.
    """
    def __init__(self, name):
        self.name = self._validate_name(name)
        self.result = None

    def convert(self):
        """
        Simple string converting using naive approach that every lowercase ASCII character
        has it's numeric representation. Additionally, most of the lowercase characters (that are handled here)
        have 3 digit representation. By simply concatenating their numbers
        we get a unique representation, which is also reversible.
        Additional processing is performed on 2 digit representations.
        :return: Numeric representation of a string as a string
        :rtype: str
        """
        str_ord_map = map(lambda x: self._get_number_repr(x), self.name)
        self.result = ''.join(str_ord_map)
        self._adjust_first_char()
        return self.result

    @staticmethod
    def _get_number_repr(x):
        repr = str(ord(x))
        l = len(repr)
        if l < 3:
            repr = '0'*(3-l) + repr
        elif l > 3:
            raise WrongNameFormat('Please use only ASCII characters')
        return repr

    def _adjust_first_char(self):
        """ Appends minus to the first letter if has less than 0 """
        if self.result.startswith('0'):
            self.result = self.result.replace('0', '-', 1)

    @staticmethod
    def _validate_name(name):
        """
        Name values cannot be:
            - empty strings or None
            - numbers
            - contain upper case characters
        WrongNameFormat is raised if any of above fails.
        :param name: value to validate
        :type name: str
        :return: name if all validators are passed, raise WrongNameFormat instead
        :rtype: str
        """
        if not name:
            raise WrongNameFormat('City name can\'t be an empty string!')
        if not isinstance(name, str):
            raise WrongNameFormat('City name must be a text string!')
        lower = name.lower()
        if lower != name:
            raise WrongNameFormat('Name must be all lowercase. Try "{}" instead.'.format(lower))
        return name
