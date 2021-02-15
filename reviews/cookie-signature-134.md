---
Publication-State: Active
Access: Public
Reviewers:
- Name: unknown
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/cookie-signature
Review-Date: '2016-08-29'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Timing attack vulnerability*<br><br>Upgrade to 1.0.6 or latest
### Details
Cookie-signature is a library for signing cookies.  Versions before 1.0.4 were vulnerable to timing attacks.
<br><br>• Affected Versions: <=1.0.5
<br>• Patched Versions: >=1.0.6
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/tj/node-cookie-signature/commit/39791081692e9e14aa62855369e1c7f80fbfd50e']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
