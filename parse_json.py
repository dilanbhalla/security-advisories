import os
import json
import glob

core = './core'
ecosystem = './ecosystem'

def parse_core(path):
    
    data = {}
    json_data = json.dumps(data)

    for filename in glob.glob(os.path.join(path, '*.json')):
        with open(filename, encoding='utf-8', mode='r') as currentFile:
            vuln = json.load(currentFile)
            data[filename] = vuln
            break
            
    json_data = json.dumps(data, indent = 3).replace("\\n"," ")
    print(json_data)
    return json_data

def parse_npm(path):

    data = {}
    json_data = json.dumps(data)

    for (dirpath, _, filenames) in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, encoding='utf-8', mode='r') as currentFile:
                vuln = json.load(currentFile)
                dirpath = os.path.join(dirpath, "")
                data[dirpath] = vuln

    json_data = json.dumps(data, indent = 3).replace("\\n"," ")
    print(json_data)
    return json_data

def json_parser():

    parse_core(core)
    # parse_npm(ecosystem)

def main():
    json_parser()

if __name__ == '__main__':
    main()
        