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

    first = False

    for (dirpath, _, filenames) in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, encoding='utf-8', mode='r') as currentFile:
                vuln = json.load(currentFile)
                dirpath = os.path.join(dirpath, "")
                data[dirpath] = vuln

                first = True
                break
        if first: break

    json_dump = json.dumps(data, indent=3, sort_keys=True).replace("\\n"," ")
    json_data = json.loads(json_dump)

    print(json_data)
    return json_data

def json_parser():

    ecosystem_output = parse_npm(ecosystem)
    # core_output = parse_core(core)

    with open('./ecosystem_output.json', 'w') as output_file:
        json.dump(ecosystem_output, output_file, indent=3, sort_keys=True)
    # with open('./core_output.json', 'w') as output_file:
    #     json.dump(core_output, output_file, indent=3, sort_keys=True)


def main():
    json_parser()

if __name__ == '__main__':
    main()
