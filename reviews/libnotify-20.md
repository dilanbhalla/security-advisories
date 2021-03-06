---
Publication-State: Active
Access: Public
Reviewers:
- Name: Adam Baldwin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/libnotify
Review-Date: '2013-05-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Potential Command Injection*<br><br>### Details
Untrusted input passed in the call to libnotify.notify could result in execution of shell commands. Callers may be unaware of this.  ### Example ``` var libnotify = require('libnotify') libnotify.notify('UNTRUSTED INPUT', { title: \"\" }, function () {     console.log(arguments); }) ```  Special thanks to Neal Poole for submitting the pull request to fix this issue.
<br><br>• Affected Versions: <= 1.0.3
<br>• Patched Versions: >= 1.0.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
