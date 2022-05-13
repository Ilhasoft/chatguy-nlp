from fastapi import FastAPI
from models.models import InputModel
import csv
from handlers import classifier
import logging


logging.basicConfig(
    filename = 'logfile.log',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger()

router = FastAPI()

pten_pipeline, enpt_pipeline = classifier.create_model()


@router.post(r'/suggest_words/')
async def classify_myth(userInput: InputModel):
    try:
        if userInput:
            keys = userInput.texts
            for i in range(len(keys)):
                if keys[i]['generate']:
                    keys[i]['suggestions'] = classifier.get_synonyms(keys[i]['word'])
                else:
                    keys[i]['suggestions'] = keys[i]['word']
            return keys

    except Exception as e:
        logger.error("-" +  str(e.__class__) + "occurred while running /suggest_words/.")


@router.post(r'/suggest_sentences/')
async def classify_myth(userInput: InputModel):
    try:
        if userInput.texts:
            key = userInput.texts
            print(key)
            lista = []
            for i in range(len(key)):
                lista.append(key[i]['suggestions'])
            flat_list = [item for sublist in lista for item in sublist]
            print('este eh o lista: ', flat_list)
            suggest_list = classifier.list_suggesting(key)
            print(suggest_list)
            result = classifier.phrase_aug(suggest_list, pten_pipeline, enpt_pipeline)
            print(result)
            return result
    except Exception as e:
        logger.error("-" + str(e.__class__) + "occurred while running /suggest_sentences/.")