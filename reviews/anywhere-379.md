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
- pkg:npm/anywhere
Review-Date: '2018-02-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-Site Scripting (XSS) - Stored*<br><br>Recommendation: update anywhere to 1.5.0 or higher
### Details
anywhere suffers from an XSS where an iframe element with url to malicious HTML file (with eg. JavaScript malware) can be used as filename and served
<br><br>• Affected Versions: <1.5.0
<br>• Patched Versions: >=1.5.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/309394', 'https://github.com/JacksonTian/anywhere/issues/33#issuecomment-366527448']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
