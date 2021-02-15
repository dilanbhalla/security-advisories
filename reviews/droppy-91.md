---
Publication-State: Active
Access: Public
Reviewers:
- Name: Craig Arendt
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/droppy
Review-Date: '2016-03-28'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*No CSRF Validation*<br><br>Upgrade to droppy version 3.5.0 or greater.
### Details
Droppy versions <=3.4.0 does not perform any verification for cross-domain websocket requests. An attacker is able to make a specially crafted page that can send requests as the context of the currently logged in user. For example this means the malicious user could add a new admin account under his control and delete others.
<br><br>• Affected Versions: <3.5.0
<br>• Patched Versions: >=3.5.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
