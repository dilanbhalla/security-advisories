---
Publication-State: Active
Access: Public
Reviewers:
- Name: Matteo Collina
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/aedes
Review-Date: '2018-08-07'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Improper Authorization*<br><br>Update aedes module to version >= 0.35.1
### Details
Aedes does not respect its own authorization rules when a client sets a Last Will
<br><br>• Affected Versions: <=0.35.0
<br>• Patched Versions: >=0.35.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/mcollina/aedes/issues/211', 'https://github.com/mcollina/aedes/issues/212']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
