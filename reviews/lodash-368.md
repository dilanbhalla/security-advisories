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
- pkg:npm/lodash
Review-Date: '2018-02-12'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*lodash prototype pollution*<br><br>Update module to 4.17.5 or higher
### Details
lodash node module before 4.17.5 suffers from a prototype pollution vulnerability via 'defaultsDeep', 'merge', and 'mergeWith' functions, which allows a malicious user to modify the prototype of 'Object' via __proto__, causing the addition or modification of an existing property that will exist on all objects.
<br><br>• Affected Versions: <4.17.5
<br>• Patched Versions: >=4.17.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/310443']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
