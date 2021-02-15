---
Publication-State: Active
Access: Public
Reviewers:
- Name: David Kirchner
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/tough-cookie
Review-Date: '2016-07-22'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*ReDoS via long string of semicolons*<br><br>Recommendation: Upgrade to at least version 2.3.0
### Details
Tough-cookie is a cookie parsing and management library.  Versions 0.9.7 through 2.2.2 contain a vulnerable regular expression that, under certain conditions involving long strings of semicolons in the "Set-Cookie" header, causes the event loop to block for excessive amounts of time.
<br><br>• Affected Versions: >=0.9.7 <=2.2.2
<br>• Patched Versions: >=2.3.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
