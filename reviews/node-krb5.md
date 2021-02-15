---
Publication-State: Active
Access: Public
Reviewers:
- Name: Richard Silverman
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/node-krb5
Review-Date: '2016-08-04'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Spoofing attack due to unvalidated KDC*<br><br>Consider using the "[kerberos](https://www.npmjs.com/package/kerberos)" npm module, which has this protection in place, or short of that, ensure there are no untrusted users on your network.
### Details
This module does not validate the KDC, which might allow an attacker with network access and enough time to spoof the KDC and impersonate a valid user without knowing their credentials.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/qesuto/node-krb5/issues/13', 'http://archive.hack.lu/2010/Bouillon-Stealing-credentials-for-impersonation.pdf']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
