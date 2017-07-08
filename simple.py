"""
:created on: 2017-07-08

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""

from flask import Flask, render_template, request, url_for

from .converter import ConvertCityName, WrongNameFormat
from .decryptor import DecryptCityNumber, WrongNumberFormat


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    """ Base routing app for main page view """
    url_for('static', filename='bootstrap.min.css')
    if request.method == 'POST':
        name = request.form.get('city', '')
        if name:
            return ConvertPostHandler.handle(name)
        number = request.form.get('number', '')
        if number:
            return DecryptPostHandler.handle(number)
    return render_template('simple_main.html')


class PostRequestHandler(object):
    """ Common class for request handling """
    parser = None
    exception = None
    prefix = ''
    template = 'simple_main.html'

    @classmethod
    def handle(cls, value):
        try:
            name = value.strip()
            c = cls.parser(value)
            result = c.parse()
            return render_template(cls.template, **cls._get_success_kwargs(name, result))
        except cls.exception as e:
            return render_template(cls.template, **cls._get_error_kwargs(e))

    @classmethod
    def _get_success_kwargs(cls, value, result):
        return {
            cls.prefix + 'ed': True,
            cls.prefix + '_input': value,
            cls.prefix + '_result': result
        }

    @classmethod
    def _get_error_kwargs(cls, exc):
        return {
            cls.prefix + '_error': True,
            cls.prefix + '_error_info': exc
        }


class ConvertPostHandler(PostRequestHandler):
    parser = ConvertCityName
    exception = WrongNameFormat
    prefix = 'convert'


class DecryptPostHandler(PostRequestHandler):
    parser = DecryptCityNumber
    exception = WrongNumberFormat
    prefix = 'decrypt'
