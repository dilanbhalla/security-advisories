---
Publication-State: Active
Access: Public
Reviewers:
- Name: Riku Keski-Keturi
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/nhouston
Review-Date: '2014-11-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>It is recommended that a different module be used, as we have been unable to reacher the maintainer of this module. We will continue to reach out to them, and if an update becomes available that fixes the issue, we will update this advisory accordingly.
### Details
All versions of the static file server module nhouston are vulnerable to directory traversal. An attacker can provide input such as `../` to read files outside of the served directory.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://en.wikipedia.org/wiki/Directory_traversal_attack']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
