---
Publication-State: Active
Access: Public
Reviewers:
- Name: Sébastian Dejonghe
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/mysql
Review-Date: '2015-12-28'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*SQL Injection due to unescaped object keys*<br><br>Recommendation: Update to the latest version of the mysql module. At least version v2.0.0-alpha8 or greater to address this issue.
### Details
Keys of objects are not escaped with `mysql.escape()` which could lead to SQL Injection.
<br><br>• Affected Versions: <=v2.0.0-alpha7
<br>• Patched Versions: >=v2.0.0-alpha8
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/felixge/node-mysql/issues/342']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
