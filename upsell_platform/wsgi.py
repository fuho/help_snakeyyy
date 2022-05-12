import logging
import sys

from dynoscale.wsgi import DynoscaleWsgiApp
from flask import Flask

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(
    logging.Formatter(
        fmt="%(asctime)s.%(msecs)03d %(levelname)-8s %(processName)s %(threadName)10s"
            " %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
)
logging.getLogger("").handlers = [handler]
logging.getLogger("dynoscale").setLevel(logging.DEBUG)

application = Flask(__name__)


@application.route("/")
def index():
    return "index"
