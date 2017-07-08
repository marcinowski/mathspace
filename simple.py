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
            return _handle_name(name)
        number = request.form.get('number', '')
        if number:
            print(type(number))
            return _handle_number(number)
    return render_template('simple_main.html')


def _handle_name(name):
    try:
        c = ConvertCityName(name)
        number = c.parse()
        return render_template('simple_main.html', converted=True, convert_input=name, convert_result=number)
    except WrongNameFormat as e:
        return render_template('simple_main.html', convert_error=True, convert_error_info=e)


def _handle_number(number):
    try:
        c = DecryptCityNumber(number)
        name = c.parse()
        return render_template('simple_main.html', decrypted=True, decrypt_input=number, decrypt_result=name)
    except WrongNumberFormat as e:
        return render_template('simple_main.html', decrypt_error=True, decrypt_error_info=e)
