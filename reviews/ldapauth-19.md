---
Publication-State: Active
Access: Public
Reviewers:
- Name: David Black, Jerome Touffe-Blin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/ldapauth
Review-Date: '2015-09-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*LDAP Injection*<br><br>Consider updating to use [ldapauth-fork](https://www.npmjs.com/package/ldapauth-fork) 2.3.3 or greater as ldapauth has not yet been patched.
### Details
ldapauth versions <= 2.2.4 are vulnerable to ldap injection through the username parameter.
<br><br>• Affected Versions: <=2.2.4
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://www.openwall.com/lists/oss-security/2015/09/18/4']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
