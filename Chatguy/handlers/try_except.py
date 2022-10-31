from fastapi import FastAPI
import logging
from functools import wraps


logger = logging.getLogger()

def error_handling(func):
    ''' 
    Function to deal with errors
    Try and except
    and show error message
    '''
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            logger.error("-" + str(e) +
                         "occurred while running /test/.")#.format(name_generator))
    return inner
