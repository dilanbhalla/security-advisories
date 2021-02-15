---
Publication-State: Active
Access: Public
Reviewers:
- Name: Björn Kimminich
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/gitbook
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross Site Scripting*<br><br>Update to version 3.2.2 or later
### Details
GitBook is a command line tool (and Node.js library) for building beautiful books using GitHub/Git and Markdown (or AsciiDoc).   Stored Cross-Site-Scripting (XSS) is possible by including code outside of backticks in any ebook. This code will be executed on the online reader.
<br><br>• Affected Versions: <3.2.2
<br>• Patched Versions: >=3.2.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/GitbookIO/gitbook/issues/1609']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
