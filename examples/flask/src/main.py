from flask import Flask

application = Flask('wrocpy')


@application.route('/flask')
def hello():
    return 'Hello world'
