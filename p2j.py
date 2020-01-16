#!/usr/local/bin/python3
'''
Convert a pkl file into json file
'''
import sys
import os
import _pickle as pickle
import json


def convert_dict_to_json(file_path):
    with open(file_path, 'rb') as fpkl, open('%s.json' % file_path, 'w') as fjson:
        data = pickle.load(fpkl)
        json.dump(data, fjson, ensure_ascii=False, sort_keys=True, indent=4)


def main():
    file_path = './lib_history.pickle'
    if os.path.isfile(file_path):
        print("Processing %s ..." % file_path)
        convert_dict_to_json(file_path)
    else:
        print("Usage: %s abs_file_path" % (__file__))


if __name__ == '__main__':
    main()


# Source/credit to https://gist.github.com/Samurais/567ebca0f59c612eb977065008aad867#file-pkl_to_json-py
#
