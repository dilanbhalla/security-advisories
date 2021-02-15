---
Publication-State: Active
Access: Public
Reviewers:
- Name: Benoit Côté-Jodoin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/flintcms
Review-Date: '2018-08-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Privilege Escalation*<br><br>Update flintcms module to version >=1.1.0
### Details
[flintcms] Account takeover due to blind MongoDB injection in password reset
<br><br>• Affected Versions: <=1.1.9
<br>• Patched Versions: >=1.1.10
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/386807']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
