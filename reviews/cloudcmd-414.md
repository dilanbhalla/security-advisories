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
- pkg:npm/cloudcmd
Review-Date: '2018-04-25'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-site Scripting (XSS) - Generic*<br><br>Recommendation: update cloudcmd module to 9.1.6 or higher
### Details
[cloudcmd] Stored XSS in the filename when directories listing
<br><br>• Affected Versions: <=9.1.5
<br>• Patched Versions: >=9.1.6
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/341044', 'https://github.com/coderaiser/cloudcmd/commit/23f4d4702cd3d473977285f26ea2ae7206b45f38']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
