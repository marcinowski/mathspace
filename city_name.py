"""
:created on: 2017-07-08

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""


class WrongNameFormat(Exception):
    """"""


class ConvertCityName(object):
    def __init__(self, name):
        self.name = self._validate_name(name)

    def convert(self):
        return self.name

    @staticmethod
    def _validate_name(name):
        if not name:
            raise WrongNameFormat('City name can\'t be an empty string!')
        if not isinstance(name, str):
            raise WrongNameFormat('City name must be a text string!')
        lower = name.lower()
        if lower != name:
            raise WrongNameFormat('Name must be all lowercase. Try {} instead.'.format(lower))

