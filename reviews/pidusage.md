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
- pkg:npm/pidusage
Review-Date: '2017-06-05'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Command Injection*<br><br>Update to version 1.1.5 or later.  Otherwise, before passing any untrusted data to the `stat` function, ensure that the data is sanitized using a proper shell escaping library. Note that Windows and Linux are not vulnerable.
### Details
pidusage is a module for cross-platform process cpu % and memory usage of a PID.  The pidusage module passes unsanitized input to child_process.exec, resulting in command injection in the ps method, as the pid is never cast to an integer as the comment expects. This module is vulnerable to this PoC on Darwin, SunOS, FreeBSD, and AIX. Windows and Linux are not vulnerable.   Proof of Concept: ``` var pid = require('pidusage'); pid.stat('1 && /usr/local/bin/python'); ```
<br><br>• Affected Versions: <=1.1.4
<br>• Patched Versions: >=1.1.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
