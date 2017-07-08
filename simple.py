"""
:created on: 2017-07-08

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""

from flask import Flask, render_template, request, url_for
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    """ Base routing app for main page view """
    url_for('static', filename='bootstrap.min.css')
    if request.method == 'POST':
        try:
            name = request.form.get('city', '')
            number = ConvertCityName().convert(name)
            return render_template('simple_main.html', results=True, number=number)
        except Exception as e:
            return render_template('simple_main.html', error=True, reason=e)
    return render_template('simple_main.html')


class ConvertCityName(object):
    def __init__(self):
        pass

    def convert(self, name):
        return name
