"""Inside this script the logging functionality are created"""

import logging


logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)


def information_logger():
    """Setting of the inforamtion logger"""
    info_logger = logging.getLogger(__name__)
    i_handler = logging.StreamHandler()
    i_handler.setLevel(logging.INFO)
    i_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
    i_handler.setFormatter(i_format)
    info_logger.addHandler(i_handler)
    info_logger.propagate = False
    return info_logger


def file_logger(file_name: str):
    """Setting logger to write a .log file"""
    f_logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler(f"{file_name}")
    f_handler.setLevel(logging.INFO)
    f_format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s")
    f_handler.setFormatter(f_format)
    f_logger.addHandler(f_format)
    f_logger.propagate = False
    return f_logger
