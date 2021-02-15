---
Publication-State: Active
Access: Public
Reviewers:
- Name: Fedot Praslov
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/node-uuid
Review-Date: '2016-03-28'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Insecure Entropy Source - Math.random()*<br><br>Upgrade to version 1.4.4 or greater
### Details
node-uuid prior to 1.4.4 contained a bug that caused it to consistently fall back to using `Math.random` instead of a more cryptographically sound source of entropy, the native `crypto` module.
<br><br>• Affected Versions: <1.4.4
<br>• Patched Versions: >=1.4.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/broofa/node-uuid/issues/108', 'https://github.com/broofa/node-uuid/issues/122']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
