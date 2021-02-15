---
Publication-State: Active
Access: Public
Reviewers:
- Name: Ron Perris
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/react-svg
Review-Date: '2018-04-27'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-site Scripting (XSS) - Generic*<br><br>Update react-svg module to 2.2.18 or higher.
### Details
[react-svg] Scripts found in SVG files are run by default.
<br><br>• Affected Versions: <=2.2.17
<br>• Patched Versions: >=2.2.18
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/tanem/react-svg/pull/57']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
