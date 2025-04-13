from src.custom_Exception import CustomException
from src.logger import get_logger
import sys

logger = get_logger(__name__)

def divide_two_number(a, b):
    try:
        result = a/b # because if b is zero then a/b will raise error
        logger.info("Dividing two numbers")
        return result
    except Exception as e:
        logger.error("Error was occcured")
        raise CustomException("Custom Error zero", sys) # we are able to capture custom error
    

if __name__ == '__main__':  # whenever we run this file the execution will start from this block
    try:
        logger.info("Main method was started")
        final_result = divide_two_number(10, 1)
    except Exception as ce:
        logger.error(str(ce))

 