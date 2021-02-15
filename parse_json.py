import os
import json
import glob

core = './core'
ecosystem = './ecosystem'

def retrieve_data(json_data, vuln_file):

    vuln = json_data[vuln_file]
    author_name = vuln['author']['name']
    author_username = vuln['author']['username']
    author_website = vuln['author']['website']
    coordinating_vendor = vuln["coordinating_vendor"][1:] if vuln["coordinating_vendor"] else None
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

    cvss_score = str(cvss_score) if cvss_score else None
    id = str(id) if id else None

    return (author_name, author_username, author_website, coordinating_vendor, created_at,
    cves, cvss_score, cvss_vector, id, module_name, overview, patched_versions,
    publish_date, recommendation, references, title, updated_at, vulnerable_versions)

def convert_to_markdown(json_data):

    num_success, num_failed, succeeded, failed = 0, 0, [], []
    for vuln_file in json_data:
        try:
            (author_name, author_username, author_website, coordinating_vendor, created_at, cves,
            cvss_score, cvss_vector, id, module_name, overview, patched_versions, publish_date,
            recommendation, references, title, updated_at, vulnerable_versions) = retrieve_data(json_data, vuln_file)
            num_success += 1
            succeeded.append(str(vuln_file))
        except:
            # print("Could not retrieve all data from " + str(vuln_file))
            num_failed += 1
            failed.append(str(vuln_file))
            continue

        # print(author_name)
        # print(author_username)
        # print(author_website)
        # print(coordinating_vendor)
        # print(created_at)
        # print(cves)
        # print(cvss_score)
        # print(cvss_vector)
        # print(id)
        # print(module_name)
        # print(overview)
        # print(patched_versions)
        # print(publish_date)
        # print(recommendation)
        # print(references)
        # print(title)
        # print(updated_at)
        # print(vulnerable_versions)
        # print("\n\n")

    print("\nCONVERSION: \nSucceeded: " + str(num_success) + ", Failed: " + str(num_failed) + "\n")

# Needs fixing use parse_npm structure to make fixes here
# def parse_core(path):
#
#     data = {}
#     json_data = json.dumps(data)
#
#     for filename in glob.glob(os.path.join(path, '*.json')):
#         with open(filename, encoding='utf-8', mode='r') as currentFile:
#             vuln = json.load(currentFile)
#             data[filename] = vuln
#             break
#
#     json_dump = json.dumps(data, indent = 3).replace("\\n"," ")
#     json_data = json.loads(json_dump)
#     print(json_data)
#     return json_data

def parse_npm(path):

    data = {}
    json_data = json.dumps(data)

    # for testing, remove after
    start, stop = 1, 10000

    num_success, num_failed, succeeded, failed = 0, 0, [], []
    count = 0

    for (dirpath, _, filenames) in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, encoding='utf-8', mode='r') as currentFile:

                vuln = json.load(currentFile)
                try:
                    test_data = {dirpath : vuln}
                    test_json_dump = json.dumps(test_data, indent=3, sort_keys=True).replace("\\n"," ")
                    test_json_data = json.loads(test_json_dump)
                    num_success += 1
                    succeeded.append(os.path.join(dirpath, ""))
                except:
                    num_failed += 1
                    failed.append(os.path.join(dirpath, ""))
                    continue

                dirpath = os.path.join(dirpath, "")

                if dirpath in data:
                    count += 1
                data[dirpath] = vuln

                start += 1
                if start == stop: break
        if start == stop: break

    print("\nPARSE: \nSucceeded: " + str(num_success) + ", Failed: " + str(num_failed))
    # print("Succeded: " + str(succeeded))
    # print("Failed: " + str(failed))

    json_dump = json.dumps(data, indent=3, sort_keys=True).replace("\\n"," ")
    # print(json_dump)
    json_data = json.loads(json_dump)
    print("Length of Data: " + str(len(json_data)))
    print("Number of Duplicates: " + str(count))
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
