from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models import InputSentences, InputWords
import csv
from handlers import classifier
import logging


logging.basicConfig(
    filename = 'logfile.log',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger()

router = FastAPI()

origins = ["*"]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pten_pipeline, enpt_pipeline = classifier.create_model()


@router.post(r'/suggest_words/')
async def suggest_words(userInput: InputWords):
    try:
        if userInput:
            keys = userInput.texts
            for i in range(len(keys)):
                if keys[i]['generate']:
                    keys[i]['suggestions'] = classifier.get_synonyms(keys[i]['word'])
                elif isinstance(keys[i]['word'], list):
                    keys[i]['suggestions'] = keys[i]['word']
                else:
                    keys[i]['suggestions'] = [keys[i]['word']]
            return keys

    except Exception as e:
        logger.error("-" +  str(e.__class__) + "occurred while running /suggest_words/.")


@router.post(r'/suggest_sentences/')
async def suggest_sentences(userInput: InputSentences):
    try:
        if userInput.texts:
            key = userInput.texts
            lista = []
            for i in range(len(key)):
                if not key[i]['entity']:
                    entity = ['nada']    
                else:
                    entity = key[i]['entity']
                lista.append(key[i]['suggestions'])
            flat_list = [item for sublist in lista for item in sublist]
            if not flat_list:
                flat_list = ['aaa']
            suggest_list = classifier.list_suggesting(key)
            result = classifier.phrase_aug(suggest_list, pten_pipeline, enpt_pipeline)
            list_words = flat_list
            obj_dict = []
            entity_keys = ['start','end','value','entity']
            main_keys = ['text', 'intent', 'entities']
            values = []
            intent = userInput.intent
            texts = list(dict.fromkeys(result))
            if userInput.isquestion:
                texts = [w[:-1]+'?' for w in texts]

            for i in range(len(texts)):
                main_dict = []
                for word in list_words:
                    try:
                        idx = texts[i].find(word)
                        entities = []
                        values = []
                        if idx > -1:
                            values.extend([idx, idx + len(word) - 1, word, entity])
                            entities.append(dict(zip(entity_keys, values)))
                            main_dict.extend([texts[i], intent, entities])
                            obj_dict.append(dict(zip(main_keys, main_dict)))
                            break
                    except:
                        pass
            json_file = {"rasa_nlu_data":{"regex_features":[],"entity_synonyms":[],"common_examples": []}}
            json_file['rasa_nlu_data']['common_examples'] = obj_dict

            return json_file
    except Exception as e:
        print(str(e.__class__))
        logger.error("-" + str(e.__class__) + "occurred while running /suggest_sentences/.")