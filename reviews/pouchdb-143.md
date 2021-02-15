---
Publication-State: Active
Access: Public
Reviewers:
- Name: micaksica
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/pouchdb
Review-Date: '2016-10-17'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Arbitrary Code Injection*<br><br>Recommendation: Update to version 6.0.5 or later.
### Details
An arbitrary code injection vector was found in PouchDB 5.4.5 and lesser via the map/reduce functions used in PouchDB temporary views and design documents. The code execution engine for this branch is not properly sandboxed and may be used to run arbitrary JavaScript as well as system commands.
<br><br>• Affected Versions: <=6.0.4
<br>• Patched Versions: >=6.0.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
