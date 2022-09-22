import pytest
import json
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


def suggest_sentences(userInput: InputSentences):
        if userInput.texts:
            result_sentence = text_generators.generate_sentences(userInput)
        return result_sentence

# Test Generate Sentence - Test 3
def test_sentence(userInput, suggest_sentences):
    if userInput.texts:
        result_sentence = text_generators.generate_sentences(userInput)
    assert result_sentence() == ({
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
    } )
        


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