---
Publication-State: Active
Access: Public
Reviewers:
- Name: Reid Burke
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/yar
Review-Date: '2014-06-16'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of Service*<br><br>Recommendation: Update to a version 2.2.0 or greater.
### Details
Yar uses an encrypted cookie for session support, during the hapi request/reply flow if this cookie value is invalid (changed by the end-user), a request object variable is not set. In versions prior 2.2.0, the presence of this variable was not validated prior to use, resulting in an unhandled ReferenceError, which in most cases will crash the process.
<br><br>• Affected Versions: <2.2.0
<br>• Patched Versions: >=2.2.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/spumko/yar/issues/34']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
