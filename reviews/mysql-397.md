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
- pkg:npm/mysql
Review-Date: '2018-03-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Remote Memory Exposure*<br><br>update mysql to 2.14.0 or higher
### Details
Affected versions of `mysql` package allocate and send an uninitialized memory chunk over network when a number is used as a password.  Only `mysql` running on Node.js versions below 6.0.0 is affected due to a throw added at Node.js side in newer versions.  PoC: ``` require('mysql').createConnection({   host     : 'localhost',   user     : 'user',   password : 1e6,   database : 'my_db' }).connect(); ```  Reported at 2017-03-15.
<br><br>• Affected Versions: >=2.0.0-alpha8 <=2.0.0-rc2 || >=2.0.0 <=2.13.0
<br>• Patched Versions: >=2.14.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/mysqljs/mysql/commit/310c6a7d1b2e14b63b572dbfbfa10128f20c6d52']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
