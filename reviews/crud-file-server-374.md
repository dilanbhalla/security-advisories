---
Publication-State: Active
Access: Public
Reviewers:
- Name: bl4de
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/crud-file-server
Review-Date: '2018-02-17'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-site Scripting (XSS) - Stored*<br><br>Recommendation: update crud-file-server to 0.8.0 or higher
### Details
crud-file-server suffers from stored XSS in filenames when directory index is served by crud-file-server
<br><br>• Affected Versions: <=0.7.0
<br>• Patched Versions: >=0.8.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/311101', 'https://github.com/omphalos/crud-file-server/commit/4155bfe068bf211b49a0b3ffd06e78cbaf1b40fa']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
