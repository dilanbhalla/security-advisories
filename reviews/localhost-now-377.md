---
Publication-State: Active
Access: Public
Reviewers:
- Name: bl4de
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/localhost-now
Review-Date: '2018-02-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Path Traversal*<br><br>Recommendation: update localhost-now to 1.0.2 or higher
### Details
localhost-now Path Traversal allows to read content of arbitrary file
<br><br>• Affected Versions: <1.0.2
<br>• Patched Versions: >=1.0.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/312889', 'https://github.com/DCKT/localhost-now/commit/30b004c7f145d677df8800a106c2edc982313995#diff-b9cfc7f2cdf78a7f4b91a753d10865a2']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
