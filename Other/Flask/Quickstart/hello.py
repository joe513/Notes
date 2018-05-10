import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/<variable>', methods=['GET', 'POST'])
def hello_world(variable=None):
    return flask.render_template('hello.html')


@app.route('/<int:number>')
def square(number):
    return '%d' % number ** 2


with app.test_request_context():
    print(flask.url_for('hello_world', variable='Bob'))


if __name__ == '__main__':
    app.run('localhost', 8080, debug=True)
