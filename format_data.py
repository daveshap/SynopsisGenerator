import os
import json


src_dir = 'descriptions/'
src_dir2 = 'synopses/'


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    files = os.listdir(src_dir)
    data = list()
    for file in files:
        first = open_file(src_dir + file).strip()
        second = open_file(src_dir2 + file).strip()
        prompt = first + '\n\nSYNOPSIS: '  # add demarc
        completion = ' ' + second + ' END'  # add stop token
        info = {'prompt': prompt, 'completion': completion}
        data.append(info)
    with open('synopsis.jsonl', 'w') as outfile:
        for i in data:
            json.dump(i, outfile)
            outfile.write('\n')