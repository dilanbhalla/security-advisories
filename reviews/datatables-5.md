---
Publication-State: Active
Access: Public
Reviewers:
- Name: Onur Yilmaz
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/datatables
Review-Date: '2015-09-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-Site Scripting*<br><br>Recommendation: Update to a version greater than 1.10.8.
### Details
Cross-site scripting (XSS) vulnerability in the DataTables plugin 1.10.8 and earlier for jQuery allows remote attackers to inject arbitrary web script or HTML via the scripts parameter to media/unit_testing/templates/6776.php.
<br><br>• Affected Versions: <=1.10.8
<br>• Patched Versions: >1.10.8
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://www.securityfocus.com/archive/1/archive/1/536437/100/0/threaded', 'https://www.netsparker.com/cve-2015-6384-xss-vulnerability-identified-in-datatables/', 'https://github.com/DataTables/DataTables/issues/602', 'https://github.com/DataTables/DataTablesSrc/commit/ccf86dc5982bd8e16d']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
