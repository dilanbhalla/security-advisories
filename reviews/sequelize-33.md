---
Publication-State: Active
Access: Public
Reviewers:
- Name: Levan Basharuli
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/sequelize
Review-Date: '2015-01-19'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*SQL Injection*<br><br>Recommendation: Update to version 2.0.0-rc8 or greater.
### Details
SQL Injection is possible in an application using the npm module sequelize if untrusted user input is passed into the order parameter.   Example: ``` Test.findAndCountAll({ where: { id :1 }, order : [['id', 'UNTRUSTED USER INPUT']] }) ```
<br><br>• Affected Versions: <=2.0.0-rc7
<br>• Patched Versions: >=2.0.0-rc8
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/sequelize/sequelize/issues/2906']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
