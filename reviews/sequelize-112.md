---
Publication-State: Active
Access: Public
Reviewers:
- Name: Spencer Creasey
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
*SQL Injection*<br><br>Recommendation: Upgrade sequelize to version 3.17.0 or greater
### Details
sequalize is an Object-relational mapping, or a middleman to convert things from Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server into usable data for NodeJS  If user input goes into the `limit` or `order` parameters, a malicious user can put in their own SQL statements.   `1; DELETE FROM "Users" WHERE 1=1; --`
<br><br>• Affected Versions: <= 3.16.0
<br>• Patched Versions: >= 3.17.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/sequelize/sequelize/pull/5167/commits/f282d85e60e3df5e57ecdb82adccb4eaef404f03']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
