import logging

from dynoscale.wsgi import DynoscaleWsgiApp
from flask import Flask

application = Flask(__name__)
ds_application = DynoscaleWsgiApp(application)


@application.route("/")
def index():
    return "index"
