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
- pkg:npm/glance
Review-Date: '2018-04-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-site Scripting (XSS) - Stored*<br><br>No fix is currently available for this vulnerability.  It is our recommendation to not install or use this module at this time.
### Details
There is a Stored XSS vulnerability in glance module. File name, which contains malicious HTML (eg. embedded iframe element or javascript: pseudoprotocol handler in <a> element) allows to execute JavaScript code against any user who opens directory listing contains such crafted file name.
<br><br>• Affected Versions: <=3.0.5
<br>• Patched Versions: None
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/310133']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
