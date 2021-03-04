import requests
import json

FILENAME = 'filename.json'
DESTINATINATION_DIR = 'files'
DEBUG = False


# HELPER FUNCTIONS

def _print(text):
    # TODO Add debug / verbose flag / accept from arg
    if DEBUG:
        print(text)

def _get_response(url):
  i = 0
  try:
    return requests.get(url, allow_redirects=True)
  except:
    i += 1
    _print(f'Retrying: {i}')
    return _get_response(url)


# MAIN CODE

with open(FILENAME) as f:
  data = json.load(f)

for row in data:
    if len(row) > 0 and row[0].startswith('http'):
        extension = row[1].split('/')[1]
        url_split = row[0].split('/')
        filenames = url_split[len(url_split) - 1].split('.')
        extension = filenames[1].split('?')[0]
        filename = filenames[0]
        _print(row[0])
        _print(f'{DESTINATINATION_DIR}/{filename}.{extension}')
        response = _get_response(row[0])
        open(f'{DESTINATINATION_DIR}/{filename}.{extension}', 'wb').write(response.content)


