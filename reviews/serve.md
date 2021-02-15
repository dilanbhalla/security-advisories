---
Publication-State: Active
Access: Public
Reviewers:
- Name: Tung Pun
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/serve
Review-Date: '2018-05-30'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Information Exposure Through Directory Listing*<br><br>Update serve module to version 7.0.0
### Details
[serve] Directory listing and File access even when they have been set to be ignored (using dot-slash)
<br><br>• Affected Versions: <= 6.5.3
<br>• Patched Versions: 7.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/330724']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
