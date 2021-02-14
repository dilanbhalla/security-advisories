import os
import json
import glob
from pprint import pprint
from Naked.toolshed.shell import execute_js, muterun_js

core = './core'
ecosystem = './ecosystem'

def parse_core(path):
    
    data = {}
    json_data = json.dumps(data)

    for filename in glob.glob(os.path.join(path, '*.json')):
        with open(filename, encoding='utf-8', mode='r') as currentFile:
            vuln = json.load(currentFile)
            data[filename] = vuln
            
    json_data = json.dumps(data, indent = 3).replace("\\n"," ")
    print(json_data)
    return json_data

def parse_npm(path):

    data = {}
    json_data = json.dumps(data)

    for (dirpath, dirnames, filenames) in os.walk(path):
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
    parse_npm(ecosystem)

    # print(result)

    # with open('counseling3.json', 'w') as output_file:
    #     json.dump(result, output_file)



def main():
    response = muterun_js('tools/vuln_valid/index.js')
    json_parser()

    # if response.exitcode == 0:
    #     json_parser(response.stdout)
    # else:
    #     sys.stderr.write(response.stderr)

if __name__ == '__main__':
    main()
        