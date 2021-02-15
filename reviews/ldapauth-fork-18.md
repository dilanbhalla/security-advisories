---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jerome Touffe-Blin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/ldapauth-fork
Review-Date: '2015-09-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*LDAP Injection*<br><br>Updated to ldapauth-fork 2.3.3 or greater.
### Details
ldapauth-fork is a module forked from node-ldapauth and is used for ldap authentication   The username parameter is not filtered as per [LDAP Escape Specifications](https://tools.ietf.org/search/rfc4515#section-3)   A malicious user is able to change their name to certain LDAP commands and run anything that they want.
<br><br>• Affected Versions: < 2.3.3
<br>• Patched Versions: >= 2.3.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/vesse/node-ldapauth-fork/issues/21', 'https://github.com/vesse/node-ldapauth-fork/commit/3feea43e243698bcaeffa904a7324f4d96df60e4']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
