import os
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

def get_logger(logfile="dundie.log"):
    """Returns a configured logger"""
    fh = handlers.RotatingFileHandler(
        logfile,
        maxBytes=300,
        backupCount=10,
    )
    fh.setLevel(LOG_LEVEL)

    #ch.setFormatter(fmt)
    fh.setFormatter(fmt)
    #log
    log.addHandler(fh)
    return log
