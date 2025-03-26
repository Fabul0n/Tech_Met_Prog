import logging
import json

class JSONFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "time": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage()
        })

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

error_handler = logging.FileHandler('./logs/errors.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
json_error_handler = logging.FileHandler('./logs/errors.json')
json_error_handler.setLevel(logging.ERROR)
json_error_handler.setFormatter(JSONFormatter())

error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
error_logger.addHandler(error_handler)
error_logger.addHandler(json_error_handler)

if __name__ == '__main__':
    error_logger.error('asd')