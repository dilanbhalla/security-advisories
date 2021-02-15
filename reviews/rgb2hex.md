---
Publication-State: Active
Access: Public
Reviewers:
- Name: Сковорода Никита Андреевич
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/rgb2hex
Review-Date: '2018-04-28'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of Service*<br><br>Update to version 0.1.6 or later
### Details
`rgb2hex` is vulnerable to ReDoS when parsing crafted invalid colors
<br><br>• Affected Versions: <0.1.6
<br>• Patched Versions: >=0.1.6
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/319629', 'https://github.com/christian-bromann/rgb2hex/blob/v0.1.0/index.js#L25', 'https://github.com/christian-bromann/rgb2hex/commit/9e0c38594432edfa64136fdf7bb651835e17c34f']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
