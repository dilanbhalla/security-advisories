---
Publication-State: Active
Access: Public
Reviewers:
- Name: Сковорода Никита Андреевич
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/base64-url
Review-Date: '2018-05-12'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Out-of-bounds Read*<br><br>Recommendation: update base64-url to 2.0.0 or higher
### Details
`base64-url` below 2.0 allocates uninitialized Buffers when number is passed in input
<br><br>• Affected Versions: <=1.3.3
<br>• Patched Versions: >=2.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/321692']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
