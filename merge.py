import json

files=['json-1.json','json-2.json', 'json-3.json']

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r', encoding="utf8") as infile:
            result.extend(json.load(infile))

    with open('dataset.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)