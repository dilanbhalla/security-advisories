---
Publication-State: Active
Access: Public
Reviewers:
- Name: panic
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/hekto
Review-Date: '2018-05-20'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Open Redirect*<br><br>Recommendation: update hekto to 0.2.4 or higher
### Details
[hekto] open redirect when target domain name is used as html filename on server
<br><br>• Affected Versions: <=0.2.3
<br>• Patched Versions: >=0.2.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/320693', 'https://github.com/herber/hekto/pull/3']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
