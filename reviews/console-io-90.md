---
Publication-State: Active
Access: Public
Reviewers:
- Name: Craig Arendt
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/console-io
Review-Date: '2016-04-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Authentication Bypass*<br><br>Recommendation: Upgrade to at least version 2.3.0
### Details
console-io is a module that allows users to implement a web console in their application.   A malicious user could bypass the authentication and execute any command that the user who is running the console-io application is able to run. This means that if console-io was running from root, the attacker would have full access to the system.   This vulnerability exists because the console-io application does not configure socket.io to require authentication, which allows a malicious user to connect via a websocket to send commands and receive the response.
<br><br>• Affected Versions: <=2.2.13
<br>• Patched Versions: >=2.3.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
