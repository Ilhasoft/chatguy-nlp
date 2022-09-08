from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models import InputCorrections, InputSentences, InputWords
import csv
from handlers import classifier, db
import logging
import sqlalchemy
import os
import urllib.request
from sqlalchemy import Column, Integer, MetaData, String, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy.orm import sessionmaker

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
 
 
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']


url = 'https://'
files_json = ['config', 'special_tokens_map', 'tokenizer', 'tokenizer_config']
files_model = ['spiece']
files_bin = ['pytorch_model']

model_path = 'model'

#for file in files_json:
#    file_name = file + '.json'
#    file_save_path = os.path.join(model_path, file_name) 
#    file_path = os.path.join(url, file_name)
#    if not os.path.exists(file_save_path):
#        urllib.request.urlretrieve(file_path, file_save_path)

#for file in files_model:
#    file_name = file + '.model'
#    file_save_path = os.path.join(model_path, file_name) 
#    file_path = os.path.join(url, file_name)
#    if not os.path.exists(file_save_path):
#        urllib.request.urlretrieve(file_path, file_save_path)

#for file in files_bin:
#    file_name = file + '.bin'
#    file_save_path = os.path.join(model_path, file_name) 
#    file_path = os.path.join(url, file_name)
#    if not os.path.exists(file_save_path):
#        urllib.request.urlretrieve(file_path, file_save_path)


# pten_pipeline, enpt_pipeline = classifier.create_model()
# model = classifier.create_model_gec()

DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}'
session = db.create_db(DATABASE_URL)

@router.post(r'/suggest_words/')
def suggest_words(userInput: InputWords):
    try:
        if userInput:
            session = db.create_db(DATABASE_URL)
            print('A')
            keys = userInput.texts
            for i in range(len(keys)):
                if keys[i]['generate']:
                    print('B')
                    idx = db.get_word_index(session, keys[i]['word'])
                    print('C')
                    if idx:
                        print('D')
                        synonyms = db.get_suggest_words(session, idx[0][0])
                        print('E')
                        keys[i]['suggestions'] = [i[0] for i in synonyms]
                    else:
                        print('F')
                        synonyms = classifier.get_synonyms(keys[i]['word'])
                        keys[i]['suggestions'] = synonyms
                        print('G')
                        db.create_word(session, keys[i]['word'])
                        print('H')
                        idx = db.get_word_index(session, keys[i]['word'])
                        print('I')
                        db.create_suggestion(session, idx[0][0], synonyms)
                        print('J')

                elif isinstance(keys[i]['word'], list):
                    keys[i]['suggestions'] = keys[i]['word']
                else:
                    keys[i]['suggestions'] = [keys[i]['word']]
            session.close()
            return keys

    except Exception as e:
        print(e)
        #logger.error("-" +  str(e.__class__) + "occurred while running /suggest_words/.")


@router.post(r'/suggest_sentences/')
def suggest_sentences(userInput: InputSentences):
    try:
        if userInput.texts:
            session = db.create_db(DATABASE_URL)
            key = userInput.texts

            lista_entities = []
            lista_entities_words = []
            for i in range(len(key)):
                if key[i]['entity']:
                    lista_entities.append([key[i]['entity']])
                    lista_entities_words.append([key[i]['suggestions']])

            suggest_list = classifier.list_suggesting(key)
            #result = classifier.phrase_gec(suggest_list, model)
            result = suggest_list
            # result = classifier.phrase_aug(suggest_list, pten_pipeline, enpt_pipeline)
            obj_dict = []
            entity_keys = ['start','end','value','entity']
            main_keys = ['text', 'intent', 'entities']
            values = []
            intent = userInput.intent
            texts = list(dict.fromkeys(result))
            if userInput.isquestion:
                texts = [w +' ?' for w in texts]

            for phrase in texts:
                try:
                    entities = []
                    values = []
                    main_dict = []
                    for i, entity in enumerate(lista_entities):
                        lista_words_entity = lista_entities_words[i][0]
                        values = []
                        for word in lista_words_entity:
                            idx = phrase.find(word)
                            if idx > -1:
                                values.extend([idx, idx + len(word) - 1, word, entity[0]])
                        entities.append(dict(zip(entity_keys, values)))
                    main_dict.extend([phrase, intent, entities])
                    obj_dict.append(dict(zip(main_keys, main_dict)))

                except Exception as e:
                    logger.error("-" + str(e.__class__) + "occurred while running /suggest_sentences/.")
        
            json_file = {"rasa_nlu_data":{"regex_features":[],"entity_synonyms":[],"common_examples": []}}
            json_file['rasa_nlu_data']['common_examples'] = obj_dict
            session.close()
            return json_file
    except Exception as e:
        logger.error("-" + str(e.__class__) + "occurred while running /suggest_sentences/.")

@router.post(r'/store_corrections/')
def suggest_words(userInput: InputCorrections):
    try:
        if userInput:
            session = db.create_db(DATABASE_URL)
            data = userInput.texts
            print('source',data[0])
            print('target',data[1])
            db.insert_corrections(session, data[0], data[1])
            session.close()
            return {200: 'Inserted!'}
    except Exception as e:
        logger.error("-" +  str(e.__class__) + "occurred while running /store_corrections/.")
