---
Publication-State: Active
Access: Public
Reviewers:
- Name: Alberto Martínez
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/riot-compiler
Review-Date: '2016-03-21'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Upgrade to version 2.3.22 or greater.
### Details
The riot-compiler version version 2.3.21 "has an issue in a regex (Catastrophic Backtracking) thats make it unusable under certain conditions"  It should be noted that 2.3.21 has been unpublished.  Thanks to Sven Slootweg for letting us know about this issue.
<br><br>• Affected Versions: 2.3.21
<br>• Patched Versions: >2.3.21
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/riot/compiler/issues/46']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
