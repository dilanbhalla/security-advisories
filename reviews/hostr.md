---
Publication-State: Active
Access: Public
Reviewers:
- Name: Liang Gong
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/hostr
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>Upgrade to v2.3.6 or later.
### Details
hostr is a simple web server that serves up the contents of the current directory.   There is a directory traversal vulnerability in hostr that allows an attacker to read files outside the current directory by sending `../` in the url path for GET requests.
<br><br>• Affected Versions: <=2.3.5
<br>• Patched Versions: >=2.3.6
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/henrytseng/hostr/issues/8)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
