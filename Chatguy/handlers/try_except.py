from fastapi import FastAPI
import logging
from functools import wraps


logger = logging.getLogger()


'''def type_text_generator():

    if app.suggest_words.__name__ == 'sugest_words':
        name_generator = 'suggest_words'
    if app.suggest_sentences.__name__ == 'store_corrections':
        name_generator = 'store_corrections'
    else:
        if app.suggest_sentences.__name__ == 'suggest_sentences':
                name_generator = 'suggest_sentences'
    
    return name_generator'''


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
