from flask import Flask
app = Flask(__name__)


@app.route('/<variable>')
def hello_world(variable):
    return 'Hello world! This is %s' % variable


@app.route('/<int:number>')
def square(number):
    return '%d' % number ** 2
