import logging

logging.basicConfig(level=logging.DEBUG)

class BaseLogger:

    def __init__(self):
        self.next_logger = None

    def add_logger(self, logger):

        if self.next_logger:
            self.next_logger.add_logger(logger)
        else:
            self.next_logger = logger

    def log(self, msg, log_type):
        if self.next_logger:
            self.next_logger.log(msg, log_type)

class InfoLogger(BaseLogger):
    type = logging.INFO

    def log(self, msg, log_type):
        if log_type == self.type:
            logging.info(msg)
        super().log(msg, log_type)

class DEBUGLogger(BaseLogger):
    type = logging.DEBUG

    def log(self, msg, log_type):
        if log_type == self.type:
            logging.debug(msg)
        super().log(msg, log_type)

if __name__ == '__main__':
    logger = BaseLogger()
    logger.add_logger(DEBUGLogger())
    logger.add_logger(InfoLogger())

    logger.log("print this log", logging.INFO)
    logger.log("print this log", logging.DEBUG)
