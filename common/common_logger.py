"""
A common Logging class for us to use with Acadella.
Has the benefit of a fancy formatter.
"""

import logging
import sys


class Logger:
    """
    A helper class to configure a single
    set of logging handlers for Acadella.
    If we didn't do it _once_ here, we'd end up with
    multiple logging handlers and thus duplicate logs
    (especially in test-case situations).
    """

    # I intend this class to be a singleton, as such
    # here is the global logger than all instances of
    # this class use.
    global_logger = None

    def __init__(self, default_log_level=logging.INFO):
        """
        Params:
            default_log_level - set the main logger to this. Only useful on
                                first call to this function.
        """
        if Logger.global_logger is None:
            Logger.global_logger = logging.getLogger(__name__)

            handler = logging.StreamHandler(sys.stdout)
            handler.setLevel(default_log_level)
            formatter = logging.Formatter(
                "%(asctime)s [%(filename)s:%(lineno)4s() - %(funcName)20s()]"
                " %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)

            Logger.global_logger.addHandler(handler)
            Logger.global_logger.setLevel(default_log_level)

    @staticmethod
    def get_logger(name, log_level=logging.INFO):
        """
        Provide a logger for the modules who ask for it

        Params:
            name - the name to provide to the sublogger generated
            log_level - the loglevel for the sublogger

        Returns:
            (logger) - a sublogger for use by the calling function
        """
        new_logger = Logger.global_logger.getChild(name)
        new_logger.setLevel(log_level)
        return new_logger
