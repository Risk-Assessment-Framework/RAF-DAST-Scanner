import logging
from config import Config


class RAFLogger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(Config().log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log(self, message, level=logging.INFO):
        match level:
            case logging.INFO:
                self.logger.info(message)
            case logging.WARNING:
                self.logger.warning(message)
            case logging.ERROR:
                self.logger.error(message)
            case logging.CRITICAL:
                self.logger.critical(message)
            case _:
                self.logger.debug(message)
