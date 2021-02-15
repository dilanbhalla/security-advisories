---
Publication-State: Active
Access: Public
Reviewers:
- Name: Karl Düüna
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/validator
Review-Date: '2014-11-12'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Recommendation: Update to version 3.22.1 or greater.
### Details
The validator module, versions < 3.22.1 are vulnerable to Regular Expression Denial of Service ([ReDoS](http://en.wikipedia.org/wiki/ReDoS)) in the isURL method.
<br><br>• Affected Versions: <3.22.1
<br>• Patched Versions: >=3.22.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://lab.cs.ttu.ee/dl93)', 'https://github.com/chriso/validator.js/issues/152#issuecomment-48107184', 'http://en.wikipedia.org/wiki/ReDoS']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
