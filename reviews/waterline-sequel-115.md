---
Publication-State: Active
Access: Public
Reviewers:
- Name: James Hush
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/waterline-sequel
Review-Date: '2016-10-31'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*SQL Injection*<br><br>Recommendation: Upgrade to at least version 0.5.1
### Details
waterline-sequel is a module that helps generate SQL statements for Waterline apps  Any user input that goes into Waterline's `like`, `contains`, `startsWith`, or `endsWith` will end up in waterline-sequel with the potential for malicious code.  A malicious user can input their own SQL statements that will get executed and have full access to the database.
<br><br>• Affected Versions: 0.5.0
<br>• Patched Versions: >= 0.5.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/balderdashy/waterline/issues/1219#issuecomment-157294530', 'https://www.owasp.org/index.php/SQL_Injection']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
