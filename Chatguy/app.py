from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models import InputSentences, InputWords
import csv
from handlers import classifier
import logging

import os
import urllib.request

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
 

url = 'https://weni-prod-ai-chatguy.s3.sa-east-1.amazonaws.com/'
files_json = ['config', 'special_tokens_map', 'tokenizer', 'tokenizer_config']
files_model = ['spiece']
files_bin = ['pytorch_model']

model_path = 'model'

for file in files_json:
    file_name = file + '.json'
    file_save_path = os.path.join(model_path, file_name) 
    file_path = os.path.join(url, file_name)
    if not os.path.exists(file_save_path):
        urllib.request.urlretrieve(file_path, file_save_path)

for file in files_model:
    file_name = file + '.model'
    file_save_path = os.path.join(model_path, file_name) 
    file_path = os.path.join(url, file_name)
    if not os.path.exists(file_save_path):
        urllib.request.urlretrieve(file_path, file_save_path)

for file in files_bin:
    file_name = file + '.bin'
    file_save_path = os.path.join(model_path, file_name) 
    file_path = os.path.join(url, file_name)
    if not os.path.exists(file_save_path):
        urllib.request.urlretrieve(file_path, file_save_path)


# pten_pipeline, enpt_pipeline = classifier.create_model()
model = classifier.create_model_gec()


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

            return json_file
    except Exception as e:
        logger.error("-" + str(e.__class__) + "occurred while running /suggest_sentences/.")