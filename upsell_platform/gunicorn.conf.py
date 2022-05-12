import logging
import sys

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

wsgi_app = "upsell_platform.wsgi:ds_application"
