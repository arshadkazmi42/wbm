import sys
import json

FILENAME = 'allurls.txt'
DEBUG = False


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


directory = _get_directory()

for line in sys.stdin:

    line = _clean_input(line)
    _print(line)

    with open(f'{directory}/{line}') as f:
        data = json.load(f)

        for row in data:
            if len(row) > 0 and row[0].startswith('http'):
                _print(str(row))
                print(row[0])
                with open(f'{directory}/{FILENAME}', "a") as dest_file:
                    dest_file.write(row[0])
                    dest_file.write('\n')
