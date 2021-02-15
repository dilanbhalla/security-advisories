---
Publication-State: Active
Access: Public
Reviewers:
- Name: Adam Baldwin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/fancy-server
Review-Date: '2014-11-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>Recommendation: Upgrade to version 0.1.4 or greater.
### Details
Versions less than 0.1.4 of the static file server module fancy-server are vulnerable to directory traversal. An attacker can provide input such as `../` to read files outside of the served directory.
<br><br>• Affected Versions: <0.1.4
<br>• Patched Versions: >=0.1.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://en.wikipedia.org/wiki/Directory_traversal_attack']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
