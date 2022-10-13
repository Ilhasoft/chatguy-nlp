url = 'https://'
files_json = ['config', 'special_tokens_map', 'tokenizer', 'tokenizer_config']
files_model = ['spiece']
files_bin = ['pytorch_model']

model_path = 'model'

# for file in files_json:
#    file_name = file + '.json'
#    file_save_path = os.path.join(model_path, file_name)
#    file_path = os.path.join(url, file_name)
#    if not os.path.exists(file_save_path):
#        urllib.request.urlretrieve(file_path, file_save_path)

# for file in files_model:
#    file_name = file + '.model'
#    file_save_path = os.path.join(model_path, file_name)
#    file_path = os.path.join(url, file_name)
#    if not os.path.exists(file_save_path):
#        urllib.request.urlretrieve(file_path, file_save_path)

# for file in files_bin:
#    file_name = file + '.bin'
#    file_save_path = os.path.join(model_path, file_name)
#    file_path = os.path.join(url, file_name)
#    if not os.path.exists(file_save_path):
#        urllib.request.urlretrieve(file_path, file_save_path)


# pten_pipeline, enpt_pipeline = classifier.create_model()
# model = classifier.create_model_gec()