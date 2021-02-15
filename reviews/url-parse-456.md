---
Publication-State: Active
Access: Public
Reviewers:
- Name: Ahmed
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/url-parse
Review-Date: '2018-07-30'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Open Redirect*<br><br>Update url-parse module to version >=1.4.3
### Details
url-parse package return wrong hostname 
<br><br>• Affected Versions: <1.4.3
<br>• Patched Versions: >=1.4.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/384029', 'https://github.com/unshiftio/url-parse/commit/53b1794e54d0711ceb52505e0f74145270570d5a', 'https://github.com/unshiftio/url-parse/commit/d7b582ec1243e8024e60ac0b62d2569c939ef5de', 'http://0xahmed.ninja/']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
