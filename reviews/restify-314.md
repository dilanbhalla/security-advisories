---
Publication-State: Active
Access: Public
Reviewers:
- Name: CycoPH
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/restify
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-Site Scripting (XSS)*<br><br>Recommendation: Upgrade to v4.1.0 or greater.
### Details
Restify is a framework for building REST APIs.  Using URL encoded script tags in a non-existent URL, an attacker can get script to run in some browsers.  For example, for the URL `https://localhost:3000/no5_such3_file7.pl?%22%3E%3Cscript%3Ealert(73541);%3C/script%3E` restify will return `<script>alert(73541);</script>` as part of the response, and in some browsers will run.
<br><br>• Affected Versions: >=2.0.0 <=4.0.4
<br>• Patched Versions: >=4.1.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/restify/node-restify/issues/1018)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
