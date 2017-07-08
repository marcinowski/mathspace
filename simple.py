from flask import Flask, render_template, request, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    url_for('static', filename='bootstrap.min.css')
    if request.method == 'POST':
        pass
    return render_template('simple_main.html')
