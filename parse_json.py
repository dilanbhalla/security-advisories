import os
import json
import glob

core = './core'
ecosystem = './ecosystem'

def retrieve_data(json_data):

    for vuln_file in json_data:
        vuln = json_data[vuln_file]
        author_name = vuln['author']['name']
        author_username = vuln['author']['username']
        author_website = vuln['author']['website']
        coordinating_vendor = vuln["coordinating_vendor"][1:]
        created_at = vuln["created_at"]
        cves = vuln["cves"]
        cvss_score = vuln["cvss_score"]
        cvss_vector = vuln["cvss_vector"]
        id = vuln["id"]
        module_name = vuln["module_name"]
        overview = vuln["overview"]
        patched_versions = vuln["patched_versions"]
        publish_date = vuln["publish_date"]
        recommendation = vuln["recommendation"]
        references = vuln["references"]
        title = vuln["title"]
        updated_at = vuln["updated_at"]
        vulnerable_versions = vuln["vulnerable_versions"]

        return author_name, author_username, author_website, coordinating_vendor, created_at,
        cves, cvss_score, cvss_vector, id, module_name, overview, patched_versions,
        publish_date, recommendation, references, title, updated_at, vulnerable_versions

def convert_to_markdown(json_data):
    author_name, author_username, author_website, coordinating_vendor, created_at,
    cves, cvss_score, cvss_vector, id, module_name, overview, patched_versions,
    publish_date, recommendation, references, title, updated_at, vulnerable_versions = retrieve_data(json_data)
    return

def parse_core(path):

    data = {}
    json_data = json.dumps(data)

    for filename in glob.glob(os.path.join(path, '*.json')):
        with open(filename, encoding='utf-8', mode='r') as currentFile:
            vuln = json.load(currentFile)
            data[filename] = vuln
            break

    json_dump = json.dumps(data, indent = 3).replace("\\n"," ")
    json_data = json.loads(json_dump)
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
    # print(json_dump)
    json_data = json.loads(json_dump)
    convert_to_markdown(json_data)
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
