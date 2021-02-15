---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jarda Kotěšovec
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/bassmaster
Review-Date: '2014-09-27'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Arbitrary JavaScript Execution*<br><br>Update to bassmaster version 1.5.2 or greater.
### Details
A vulnerability exists in bassmaster <= 1.5.1 that allows for an attacker to provide arbitrary JavaScript that is then executed server side via eval.
<br><br>• Affected Versions: <=1.5.1
<br>• Patched Versions: >=1.5.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://www.npmjs.org/package/bassmaster', 'https://github.com/hapijs/bassmaster/commit/b751602d8cb7194ee62a61e085069679525138c4']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
