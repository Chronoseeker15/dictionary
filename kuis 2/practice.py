import requests

api_key = '9cdb6a2c-5efe-456d-8dca-3cdb961bace8'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res  = requests.get(url)
definitions = res.json()
for definition in definitions:
    print(definition)