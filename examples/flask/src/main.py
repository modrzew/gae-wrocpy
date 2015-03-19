from flask import Flask

application = Flask('wrocpy')


@application.route('/')
def hello():
    return 'Hello world'
