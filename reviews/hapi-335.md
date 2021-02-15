---
Publication-State: Active
Access: Public
Reviewers:
- Name: Georgios Andrianakis
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/hapi
Review-Date: '2017-04-05'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of Service via malformed accept-encoding header*<br><br>Upgrade to hapi 16.1.1 or greater.
### Details
hapi is a web and services application framework.  When hapi encounters a malformed `accept-encoding` header an uncaught exception is thrown. This may cause hapi to crash or to hang the client connection until the timeout period is reached.
<br><br>• Affected Versions: >= 15.0.0 <= 16.1.0
<br>• Patched Versions: >= 16.1.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/hapijs/hapi/issues/3466']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
