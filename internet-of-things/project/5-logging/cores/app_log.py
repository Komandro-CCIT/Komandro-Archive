import logging

class AppLogger:
    def __init__(self, log_file="app.log"):
        self.__log_file = f"logs/{log_file}"
        self.__logger = logging.getLogger(__name__)
        
        if not self.__logger.handlers:
            self.__logger.setLevel(logging.INFO)
            self.file_handler = logging.FileHandler(self.__log_file)
            self.file_handler.setLevel(logging.INFO)
            self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S.%s')
            self.file_handler.setFormatter(self.formatter)
            self.__logger.addHandler(self.file_handler)

    def info(self, message):
        self.__logger.info(message)

    def warning(self, message):
        self.__logger.warning(message)

    def error(self, message):
        self.__logger.error(message)

    def critical(self, message):
        self.__logger.critical(message)