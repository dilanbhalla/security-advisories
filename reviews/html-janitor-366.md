---
Publication-State: Active
Access: Public
Reviewers:
- Name: _bayotop
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/html-janitor
Review-Date: '2018-01-23'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*html-janitor passing user-controlled data to clean() leads to XSS*<br><br>Recommendation: No fix is currently available for this vulnerability.  It is our recommendation to not install or use this module at this time.
### Details
Passing user-controlled data to the module's clean() function can result in arbitrary JS execution, because of unsafe DOM operations.
<br><br>• Affected Versions: <=2.0.2
<br>• Patched Versions: None
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/guardian/html-janitor/issues/34', 'https://hackerone.com/reports/308155']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
