import os
import json
import glob

core = './core'
ecosystem = './ecosystem'

def retrieve_data(json_data, vuln_file):

    vuln = json_data[vuln_file]

    (author_name, author_username, author_website, coordinating_vendor, created_at, cves, cvss_score, cvss_vector,
    id, module_name, overview, patched_versions, publish_date, recommendation, references, title, updated_at, vulnerable_versions) = (vuln['author']['name'],
    vuln['author']['username'], vuln['author']['website'], vuln["coordinating_vendor"], vuln["created_at"], vuln["cves"],
    vuln["cvss_score"], vuln["cvss_vector"], vuln["id"], vuln["module_name"], vuln["overview"], vuln["patched_versions"], vuln["publish_date"],
    vuln["recommendation"], vuln["references"], vuln["title"], vuln["updated_at"], vuln["vulnerable_versions"])

    cvss_score = str(cvss_score) if cvss_score else None
    id = str(id) if id else None

    return (author_name, author_username, author_website, coordinating_vendor, created_at, cves, cvss_score, cvss_vector, id,
    module_name, overview, patched_versions, publish_date, recommendation, references, title, updated_at, vulnerable_versions)

def convert_to_markdown(json_data):

    num_success, num_failed, succeeded, failed = 0, 0, [], []
    for vuln_file in json_data:
        try:
            (author_name, author_username, author_website, coordinating_vendor, created_at, cves, cvss_score, cvss_vector, id, module_name,
            overview, patched_versions, publish_date,recommendation, references, title, updated_at, vulnerable_versions) = retrieve_data(json_data, vuln_file)
            num_success += 1
            succeeded.append(str(vuln_file))
        except:
            # print("Could not retrieve all data from " + str(vuln_file))
            num_failed += 1
            failed.append(str(vuln_file))
            continue

        # print(str(author_name) + "\n" + str(author_username) + "\n" + str(author_website) + "\n" + str(coordinating_vendor) +
        # "\n" + str(created_at) + "\n" + str(cves) + "\n" + str(cvss_score) + "\n" + str(cvss_vector) + "\n" + str(id) + "\n" + str(module_name) +
        # "\n" + str(overview) + "\n" + str(patched_versions) + "\n" + str(publish_date) + "\n" + str(recommendation) + "\n" + str(references) +
        # "\n" + str(title) + "\n" + str(updated_at) + "\n" + str(vulnerable_versions) + "\n")

    print("\nCONVERSION: \nSucceeded: " + str(num_success) + ", Failed: " + str(num_failed) + "\n")


def parse_npm(path):

    data = {}
    json_data = json.dumps(data)

    # for testing, remove after
    start, stop = 1, 10000

    num_success, num_failed, succeeded, failed = 0, 0, [], []

    for (dirpath, _, filenames) in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, encoding='utf-8', mode='r') as currentFile:

                vuln = json.load(currentFile)
                try:
                    test_data = {filepath : vuln}
                    test_json_dump = json.dumps(test_data, indent=3, sort_keys=True).replace("\\n"," ")
                    test_json_data = json.loads(test_json_dump)
                    num_success += 1
                    succeeded.append(filepath)
                except:
                    num_failed += 1
                    failed.append(filepath)
                    continue

                data[filepath] = vuln

                start += 1
                if start == stop: break
        if start == stop: break

    print("\nPARSE: \nSucceeded: " + str(num_success) + ", Failed: " + str(num_failed))
    # print("Succeded: " + str(succeeded))
    # print("Failed: " + str(failed))

    json_dump = json.dumps(data, indent=3, sort_keys=True).replace("\\n"," ")
    # print(json_dump)
    json_data = json.loads(json_dump)
    # print("Length of Output: " + str(len(json_data)))
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




# For core node vulnerabilities. When ready paste this above pare_npm function and fix up (use parse_npm structure to make fixes here)
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
