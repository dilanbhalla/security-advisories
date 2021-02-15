---
Publication-State: Active
Access: Public
Reviewers:
- Name: Dinis Cruz
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/send
Review-Date: '2015-11-03'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Root Path Disclosure*<br><br>Upgrade to send version 0.11.1 or greater.
### Details
The send module < 0.11.1 discloses the root path.
<br><br>• Affected Versions: <0.11.1
<br>• Patched Versions: >=0.11.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/pillarjs/send/pull/70', 'https://github.com/expressjs/serve-static/blob/master/HISTORY.md#181--2015-01-20']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
