---
Publication-State: Active
Access: Public
Reviewers:
- Name: Alexey Tyurin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/cryo
Review-Date: '2018-06-19'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Code Injection*<br><br>Recommendation: No fix is currently available for this vulnerability.  It is our recommendation to not install or use this module at this time.
### Details
Insecure implementation of deserialization in cryo
<br><br>• Affected Versions: <=0.0.6
<br>• Patched Versions: None
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/350418']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
