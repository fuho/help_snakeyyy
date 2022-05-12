import logging
import sys

from dynoscale.hooks.gunicorn import pre_request as dynoscale_hook

log_handler = logging.StreamHandler(stream=sys.stdout)
log_handler.setFormatter(
    logging.Formatter(
        fmt="%(asctime)s.%(msecs)03d %(levelname)-8s %(processName)s %(threadName)10s"
            " %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
)
logging.getLogger("dynoscale").handlers = [log_handler]
logging.getLogger("dynoscale").setLevel(logging.DEBUG)


def pre_request(worker, req):
    # https://dynoscale.net/documentation/getting-started-python
    dynoscale_hook(worker, req)
