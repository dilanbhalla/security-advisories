---
Publication-State: Active
Access: Public
Reviewers:
- Name: orange_8361
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/resolve-path
Review-Date: '2018-02-22'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Path Traversal*<br><br>update resolve-path to 1.4.0 or higher
### Details
resolve-path relative path resolving suffers from a lack of file path sanitization for windows based paths
<br><br>• Affected Versions: <1.4.0
<br>• Patched Versions: >=1.4.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/315760', 'https://github.com/pillarjs/resolve-path/commit/fe5b8052cafd35fcdafe9210e100e9050b37d2a0']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
