import sys
import json

FILENAME = 'allurls.txt'
DEBUG = True


# HELPER FUNCTIONS

def _print(text):
    # TODO Add debug / verbose flag / accept from arg
    if DEBUG:
        print(text)

def _get_directory():
    args = sys.argv

    _print(args)

    if len(args) < 1:
        print('Directory name missing')
        exit()

    return args[1]

def _clean_input(input):

    return input.replace('\n', '')

def _is_image_url(url):

    values = url.split('?')
    
    if values[0].endswith('.png') or values[0].endswith('.jpg') or values[0].endswith('.svg') \
        or values[0].endswith('.jpeg') or values[0].endswith('.css'):
        return True

    return False

def _is_valid_url(url):

    return not _is_image_url(url)


directory = _get_directory()

for line in sys.stdin:

    line = _clean_input(line)
    _print(line)

    with open(f'{directory}/{line}') as f:
        data = json.load(f)

        for row in data:
            if len(row) > 0 and row[0].startswith('http') and _is_valid_url(row[0]):
                _print(str(row))
                print(row[0])
                with open(f'{directory}/{FILENAME}', "a") as dest_file:
                    dest_file.write(row[0])
                    dest_file.write('\n')
