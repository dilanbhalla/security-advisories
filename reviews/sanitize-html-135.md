---
Publication-State: Active
Access: Public
Reviewers:
- Name: Björn Kimminich
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/sanitize-html
Review-Date: '2016-08-01'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS - Sanitization not applied recursively*<br><br>Upgrade to 1.4.3 or later
### Details
Sanitization of HTML strings is not applied recursively to input, allowing an attacker to potentially inject script and other markup.
<br><br>• Affected Versions: <=1.4.2
<br>• Patched Versions: >=1.4.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/punkave/sanitize-html/issues/29']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
