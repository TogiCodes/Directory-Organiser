import os
import json

PATH = 'dir'

coding_list = []

def list_files(dir):
    return os.listdir(dir)

files = list_files(PATH)

f = open('extension_list.json')

data = json.load(f)


for category in data:
    for file in files:
        if '.' not in file: continue 
        if file.split('.')[1] in data[category]:
            os.mkdir(f"{PATH}/{category}")
            os.rename(f'dir/{file}', f"{PATH}/{category}/{file}")

files = list_files(PATH)


random = list(filter(lambda file: '.' in file, files))

for item in random:
    os.mkdir(f"{PATH}/Uncategorised")
    os.rename(f'dir/{item}', f"{PATH}/Uncategorised/{item}")


