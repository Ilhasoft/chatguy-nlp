
from pysinonimos.sinonimos import Search, historic
import json
import itertools
from simplet5 import SimpleT5
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

## CÓDIGO PARA ESTAR NO INIT
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

def phrase_aug(suggest_list, pten_pipeline, enpt_pipeline):
  aug_list = []
  for phrase in suggest_list:
    aa = "translate Portuguese to English: " + phrase + "."
    pten = pten_pipeline(aa)
    enpt = "translate English to Portuguese: " + pten[0]['generated_text']
    enpt = enpt_pipeline(enpt)
    aug_list.append(enpt[0]['generated_text'])
  return aug_list

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
