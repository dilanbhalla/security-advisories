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
- pkg:npm/simplehttpserver
Review-Date: '2018-02-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-Site Scripting (XSS) - Stored*<br><br>Recommendation: No fix is currently available for this vulnerability.  It is our recommendation to not install or use this module at this time.
### Details
simplehttpserver suffers from Stored XSS in file names leads to malicious JavaScript code execution when directory listing is output in HTML
<br><br>• Affected Versions: <=0.0.6
<br>• Patched Versions: None
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/309648']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
