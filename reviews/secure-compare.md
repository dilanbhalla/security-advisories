---
Publication-State: Active
Access: Public
Reviewers:
- Name: Joshua Dague
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/secure-compare
Review-Date: '2015-10-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Insecure Comparison*<br><br>Upgrade to secure-compare 3.0.1 or greater.
### Details
secure-compare 3.0.0 and below do not actually compare two strings properly.   compare was actually comparing the first argument with itself, meaning the check passed for any two strings of the same length.
<br><br>• Affected Versions: <=3.0.0
<br>• Patched Versions: >3.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/vdemedes/secure-compare/pull/1']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
