import os
import json
import glob
from mdutils.mdutils import MdUtils

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
    count = 0

    print(len(json_data))

    for vuln_file in json_data:
        try:
            (author_name, author_username, author_website, coordinating_vendor, created_at, cves, cvss_score, cvss_vector, id, module_name,
            overview, patched_versions, publish_date, recommendation, references, title, updated_at, vulnerable_versions) = retrieve_data(json_data, vuln_file)
            num_success += 1
            succeeded.append(str(vuln_file))
        except:
            # print("Could not retrieve all data from " + str(vuln_file))
            num_failed += 1
            failed.append(str(vuln_file))
            continue

        review_basename = vuln_file.split("/")[-2]
        json_basename = vuln_file.split("/")[-1].split(".")[0]
        with open("./reviews/" + str(review_basename) + "-" + str(id) + ".md", 'w') as review:

            # Metadata

            review.write("---\n")
            review.write("Publication-State: Active\n")
            review.write("Access: Public\n")
            review.write("Reviewers:\n")
            review.write("- Name: " + author_name + "\n  Associated-With-Project: false\n  Compensation-Source: external\n")
            # review.write("Associated-With-Project: false\n")
            # review.write("Compensation-Source: External\n")
            review.write("Domain: Security\n")
            review.write("Methodology:\n")
            review.write("- Code-Review\n")
            review.write("Issues-Identified: Not-Examined\n")
            review.write("Package-URLs:\n")
            review.write("- pkg:npm/" + review_basename + "\n")
            # # NOT SURE ABOUT THIS. Which date is the appropriate date to use here?
            review.write("Review-Date: '" + publish_date + "'\n")
            review.write("Scope: Implementation/Full\n")
            review.write("Schema-Version: '1.0'\n")
            review.write("SPDX-License-Identifier: CC-BY-4.0\n")
            review.write("---\n")

            # Content

            review.write("### Summary\n")
            review.write("*" + title + "*")
            review.write("<br><br>")
            if recommendation: review.write(recommendation + "\n")

            review.write("### Details\n")
            review.write(overview + "\n")
            review.write("<br><br>")
            review.write("• Affected Versions: " + str(vulnerable_versions) + "\n")
            review.write("<br>")
            review.write("• Patched Versions: " + str(patched_versions) + "\n")

            review.write("### Methodology\n")
            review.write("This review was taken directly from the Security Advisories section of npm's official website.\n")

            review.write("### External References\n")
            review.write(str(references) + "\n")

            review.write("### Disclaimer\n")
            review.write("All security reviews are conducted on a \"best-effort\" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.\n")

            review.write("### License\n")
            review.write("This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.\n")

        count += 1
        # if count == 5:
        #     break

        # print(str(author_name) + "\n" + str(author_username) + "\n" + str(author_website) + "\n" + str(coordinating_vendor) +
        # "\n" + str(created_at) + "\n" + str(cves) + "\n" + str(cvss_score) + "\n" + str(cvss_vector) + "\n" + str(id) + "\n" + str(module_name) +
        # "\n" + str(overview) + "\n" + str(patched_versions) + "\n" + str(publish_date) + "\n" + str(recommendation) + "\n" + str(references) +
        # "\n" + str(title) + "\n" + str(updated_at) + "\n" + str(vulnerable_versions) + "\n")

    print("\nMARKDOWN CONVERSION: \nSucceeded: " + str(num_success) + ", Failed: " + str(num_failed) + "\n")


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

    print("\nJSON PARSE: \nSucceeded: " + str(num_success) + ", Failed: " + str(num_failed))
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
