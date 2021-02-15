---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jamie Davis
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/is-my-json-valid
Review-Date: '2018-02-21'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service (ReDoS)*<br><br>Recommendation: update is-my-json-valid to 1.4.1, 2.17.2 or higher
### Details
is-my-json-valid is vulnerable to Regular Expression Denial of Service (ReDoS) attacks via the email validation function
<br><br>• Affected Versions: <1.4.1 || >=2.0.0 <2.17.2
<br>• Patched Versions: >=1.4.1 <2.0.0 || >=2.17.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/317548', 'https://github.com/mafintosh/is-my-json-valid/commit/b3051b277f7caa08cd2edc6f74f50aeda65d2976', 'https://github.com/mafintosh/is-my-json-valid/pull/159']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
