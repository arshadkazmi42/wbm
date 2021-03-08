import sys
import json
import requests
from urllib import parse
from requests.utils import requote_uri
from pathlib import Path


WAYBACK_URL = 'https://web.archive.org/web/timemap?url={}%2F&matchType=prefix&collapse=urlkey&output=json&fl=original%2Cmimetype%2Ctimestamp%2Cendtimestamp%2Cgroupcount%2Cuniqcount&filter=!statuscode%3A%5B45%5D..&limit=100000&_=1614823806435'
DEBUG = False


# HELPER FUNCTIONS

def _print(text):
    # TODO Add debug / verbose flag / accept from arg
    if DEBUG:
        print(text)

def _get_response(url):
  i = 0
  try:
    return requests.get(url)
  except:
    i += 1
    _print(f'Retrying: {i}')
    return _get_response(url)


def _get_input_url():

  args = sys.argv
  if len(args) == 0:
    _print('No input urls')
    sys.exit()

  return args[1]

def _get_filename(url):

  return parse.urlparse(url).hostname

def _get_directory(url):

  hostname = parse.urlparse(url).hostname
  values = hostname.split('.')

  if len(values) == 2:
      return values[0]

  if len(values) == 3:
      return values[1]

  return hostname

def _create_directory(directory):

  Path(directory).mkdir(parents=True, exist_ok=True)


# MAIN CODE

input_url = _get_input_url()
url = WAYBACK_URL.format(requote_uri(input_url))

print(input_url)
_print(url)
_print(_get_directory(input_url))

response = _get_response(url)
result = response.json()

_print(result)

filename = _get_filename(input_url)
#directory = _get_directory(input_url)

#_create_directory(directory)

_print(f'{filename}.json')

with open(f'{filename}.json', 'w') as outfile:
    json.dump(result, outfile)
