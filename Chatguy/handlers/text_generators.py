from handlers import db
from handlers import classifier
from models.models import InputCorrections, InputSentences, InputWords
from logging import Logger


def generate_words(keys, session):
    ''' 
    Function to generate new synonyms words from a input
    '''
    for i in range(len(keys)):
        if keys[i]['generate']:
            idx = db.get_word_index(session, keys[i]['word'])
            if idx:
                synonyms = db.get_suggest_words(session, idx[0][0])
                keys[i]['suggestions'] = [i[0] for i in synonyms]
            else:
                synonyms = classifier.get_synonyms(keys[i]['word'])
                keys[i]['suggestions'] = synonyms
                db.create_word(session, keys[i]['word'])
                idx = db.get_word_index(session, keys[i]['word'])
                db.create_suggestion(session, idx[0][0], synonyms)

        elif isinstance(keys[i]['word'], list):
            keys[i]['suggestions'] = keys[i]['word']
        else:
            keys[i]['suggestions'] = [keys[i]['word']]

    return keys


def generate_sentences(key, session, userInput):
    '''
    Function to generate statments from a word and entity input
    '''
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
            entity_keys = ['start', 'end', 'value', 'entity']
            main_keys = ['text', 'intent', 'entities']
            values = []
            intent = userInput.intent
            texts = list(dict.fromkeys(result))
            if userInput.isquestion:
                texts = [w + ' ?' for w in texts]

            output_sentence_format(texts)

            json_file = {"rasa_nlu_data": {"regex_features": [],
                                           "entity_synonyms": [], "common_examples": []}}
            json_file['rasa_nlu_data']['common_examples'] = obj_dict
            

            return json_file


def output_sentence_format(lista_entities, lista_entities_words, obj_dict, entity_keys, main_keys, values, intent, texts):
    for phrase in texts:
            entities = []
            values = []
            main_dict = []
            for i, entity in enumerate(lista_entities):
                lista_words_entity = lista_entities_words[i][0]
                values = []
                for word in lista_words_entity:
                    idx = phrase.find(word)
                    if idx > -1:
                        values.extend(
                            [idx, idx + len(word), word, entity[0]])
                entities.append(dict(zip(entity_keys, values)))
            main_dict.extend([phrase, intent, entities])
            obj_dict.append(dict(zip(main_keys, main_dict)))




