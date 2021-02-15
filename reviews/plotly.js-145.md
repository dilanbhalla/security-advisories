---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jared Folkins
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/plotly.js
Review-Date: '2016-10-17'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross Site Scripting (XSS)*<br><br>Update to 1.16.0 or later.
### Details
If an attacker can trick an unsuspecting user into viewing a specially crafted plot on a site that uses plotly.js, then the attacker could potentially retrieve authentication tokens and perform actions on behalf of the user.
<br><br>• Affected Versions: <1.10.4 || >=1.11.0 <1.16.0
<br>• Patched Versions: >=1.10.4 <1.11.0 || >=1.16.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://help.plot.ly/security-advisories/2016-08-08-plotlyjs-xss-advisory/', 'https://acloudtree.com/2016-08-09-how-i-hacked-plotly-by-exploiting-a-svg-vulnerability-in-plotlyjs/']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
