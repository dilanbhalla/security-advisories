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
- pkg:npm/sequelize
Review-Date: '2016-10-31'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*SQL Injection*<br><br>Upgrade to at least version <=1.7.0-alpha3
### Details
sequelize is an Object-relational mapping, or a middleman to convert things from Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server into usable data for NodeJS  Before version 1.7.0-alpha3, sequelize defaulted SQLite to use MySQL backslash escaping, even though SQLite uses Postgres escaping.
<br><br>• Affected Versions: <= 1.7.0-alpha2
<br>• Patched Versions: >= 1.7.0-alpha3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/sequelize/sequelize/commit/c876192aa6ce1f67e22b26a4d175b8478615f42d']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
