---
Publication-State: Active
Access: Public
Reviewers:
- Name: Leibale Eidelman
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
*Improper Escaping of Bound Arrays*<br><br>Recommendation: Upgrade to sequelize version 3.20.0 or greater
### Details
sequalize is an Object-relational mapping, or a middleman to convert things from Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server into usable data for NodeJS  In Postgres, SQLite, and Microsoft SQL Server there is an issue where arrays are treated as strings and improperly escaped.  This causes potential SQL injection, where a malicious user could put `["test", "'); DELETE TestTable WHERE Id = 1 --')"]` inside of ``` database.query('SELECT * FROM TestTable WHERE Name IN (:names)', {   replacements: {     names: directCopyOfUserInput   } }); ``` and cause the SQL statement to become `SELECT Id FROM Table WHERE Name IN ('test', '\'); DELETE TestTable WHERE Id = 1 --')`.   In Postgres, MSSQL, and SQLite, the backslash has no special meaning. This causes the the statement to delete whichever Id has a value of 1 in the TestTable table.
<br><br>• Affected Versions: <=3.19.3
<br>• Patched Versions: >=3.20.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/sequelize/sequelize/issues/5671']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
