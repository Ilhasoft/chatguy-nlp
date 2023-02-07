
import json
import itertools
from simplet5 import SimpleT5
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import requests
import sys
from scrapy.selector import Selector 
from unicodedata import normalize

## CÓDIGO PARA ESTAR NO INIT

def create_model_gec():  
  model = SimpleT5()
  model.from_pretrained('t5', 't5-base')
  model.load_model("t5",'./model', use_gpu=False)
  return model

def create_model():
    tokenizer_pten = AutoTokenizer.from_pretrained("unicamp-dl/translation-pt-en-t5")
    model_pten = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-pt-en-t5")
    pten_pipeline = pipeline('text2text-generation', model=model_pten, tokenizer=tokenizer_pten)
    tokenizer_enpt = AutoTokenizer.from_pretrained("unicamp-dl/translation-en-pt-t5")
    model_enpt = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-en-pt-t5")
    enpt_pipeline = pipeline('text2text-generation', model=model_enpt, tokenizer=tokenizer_enpt)
    return pten_pipeline, enpt_pipeline

def join_tuple_string(strings_tuple) -> str:
   return ' '.join(strings_tuple)

def list_suggesting(key):
  new_arr = []
  for i in range(len(key)):
    new_arr.append(key[i]['suggestions'])
  arr_new = list(itertools.product(*new_arr))
  result = map(join_tuple_string, list(arr_new))
  return list(result)

def phrase_gec(list_phrases, model):
  list_gec = []
  for phrase in list_phrases:
    phrase_gec = model.predict(phrase)
    list_gec.append(phrase_gec[0])
  return list_gec

def phrase_aug(suggest_list, pten_pipeline, enpt_pipeline):
  aug_list = []
  for phrase in suggest_list:
    aa = "translate Portuguese to English: " + phrase + "."
    pten = pten_pipeline(aa)
    enpt = "translate English to Portuguese: " + pten[0]['generated_text']
    enpt = enpt_pipeline(enpt)
    aug_list.append(enpt[0]['generated_text'])
  return aug_list


class Search(object):
	"""docstring for Search"""
	def __init__(self, palavra):
		super(Search, self).__init__()
		self.word = palavra.split(" ")

	def synonyms(self, verbose=True):
		param = "-".join(self.word)
		param = normalize('NFKD', param).encode('ASCII','ignore').decode('ASCII')
		if verbose == True:
			print("Carregando sinônimos para '{}'...".format(param))

			r = requests.get('https://www.sinonimos.com.br/{}/'.format(param))
			print(r)
			conteudo = r.content.decode('iso8859-1')
			palavra = Selector(text=conteudo).xpath('//h1[@class="h-palavra"]/text()').get()
			sinonimos = Selector(text=conteudo).xpath('//a[@class="sinonimo"]/text()').getall()
			return sinonimos[:12]


def get_synonyms(word):
  suggested = Search(word)
  suggested = suggested.synonyms()

  if suggested == 404:
    suggested = [word]
  else:
    try:
      suggested.insert(0, word)
    except Exception as e:
      return [word]

  return suggested
