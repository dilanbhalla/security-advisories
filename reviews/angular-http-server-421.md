---
Publication-State: Active
Access: Public
Reviewers:
- Name: tungpun
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/angular-http-server
Review-Date: '2018-04-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Path Traversal*<br><br>Recommendation: update angular-http-server to 1.44 or higher
### Details
[angular-http-server] Server Directory Traversal
<br><br>• Affected Versions: <=1.4.3
<br>• Patched Versions: >=1.4.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/330349', 'https://github.com/simonh1000/angular-http-server/commit/8bafc9577161469f5dea01e0b98ea9c525d063e9']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
