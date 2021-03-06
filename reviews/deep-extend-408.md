---
Publication-State: Active
Access: Public
Reviewers:
- Name: Olivier Arteau
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/deep-extend
Review-Date: '2018-04-09'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*deep-extend prototype pollution*<br><br>Recommendation: Update to version 0.5.1 or later.
### Details
deep-extend node module suffers from a prototype pollution vulnerability
<br><br>• Affected Versions: <=0.5.0
<br>• Patched Versions: >=0.5.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/311333']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
