import requests

api_key = '52b9bd8a-9a64-4783-a025-224a6a30d879'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)
definitions = res.json()

for definition in definitions:
    print(definition)