import pytest
import json
from fastapi.testclient import TestClient
from models.models import InputSentences
from handlers import text_generators
from pydantic import BaseModel


# Simple test 1
def test_one_plus_five():
    assert 1 + 5 == 6


def func(x):
    return x + 1

# Simple test 2
def test_answer():
    assert func(3) == 4




# Test Generate Sentence - Test 3
def test_sentence(client: TestClient, userInput, suggest_sentences):
    response = client.post(r'/suggest_sentences')
    key = userInput.texts
    result_sentence = text_generators.generate_sentences(userInput)
    assert result_sentence == response.json()
    '''assert result_sentence() == ({
	"rasa_nlu_data": {
		"regex_features": [],
		"entity_synonyms": [],
		"common_examples": [
			{
				"text": "há diversas homens no planeta ?",
				"intent": "teste",
				"entities": [
					{
						"start": 0,
						"end": 2,
						"value": "há",
						"entity": "existir"
					}
				]
			}]
        }
    } )'''
        
# Test Generate Sentence - Test 4
def test_sentence_output(userInput):
    key = userInput.texts
    result_sentence = text_generators.generate_sentences(key)
    assert key == result_sentence
'''
assert InputSentences(
        {"isquestion": True,
         "intent": "teste",
         "texts": [
             {
                 "word": "existem",
                 "generate": True,
                 "entity": "existir",
                 "suggestions": [
                     "há",
                     "existem"
                 ]
             }]}
    ) == ({
        "rasa_nlu_data": {
            "regex_features": [],
            "entity_synonyms": [],
            "common_examples": [
                {
                    "text": "há diversas homens no planeta ?",
                    "intent": "teste",
                    "entities": [
                        {
                            "start": 0,
                            "end": 2,
                            "value": "há",
                            "entity": "existir"
                        }
                    ]
                }
            ]}})
'''