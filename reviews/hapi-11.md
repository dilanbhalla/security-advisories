---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jo Liss
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/hapi
Review-Date: '2014-02-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*File Descriptor Leak Can Cause DoS Vulnerability*<br><br>- Please upgrade to version 2.2.x or above as soon as possible.
### Details
Versions 2.0.x and 2.1.x have a file descriptor leak that when triggered repeatedly will cause the server to run out of file descriptors and the node process to die. The effort required to take down a server depends on the process file descriptor limit. No other side effects or exploits have been identified.  ### Impact  This vulnerability allows an attacker to take down a hapi-based server running versions 2.0.x and 2.1.x.  This does NOT affect hapi 1.x deployments.
<br><br>• Affected Versions: 2.0.x || 2.1.x
<br>• Patched Versions: >= 2.2.x
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/spumko/hapi/issues/1427']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
