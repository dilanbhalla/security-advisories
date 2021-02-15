---
Publication-State: Active
Access: Public
Reviewers:
- Name: Greg Meyer
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/keystone
Review-Date: '2015-12-04'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Authentication Weakness*<br><br>Recommendation: Users of this module should update to version 0.3.16 or greater
### Details
Due to a bug in the the default sign in functionality, incomplete email addresses could be matched. A correct password is still required to complete sign in.
<br><br>• Affected Versions: <0.3.16
<br>• Patched Versions: >=0.3.16
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
