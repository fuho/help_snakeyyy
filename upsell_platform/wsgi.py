import logging
from flask import Flask

application = Flask(__name__)
application.logger.setLevel(logging.DEBUG)


@application.route("/")
def index():
    application.logger.info('################### index requested ###################')
    return "index"

