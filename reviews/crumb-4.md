---
Publication-State: Active
Access: Public
Reviewers:
- Name: Marcus Stong
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/crumb
Review-Date: '2014-08-01'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*CORS Token Disclosure*<br><br>Update to a version 3.0.0 or greater.
### Details
When CORS is enabled on a hapi route handler, it is possible to set a crumb token for a different domain. An attacker would need to have an application consumer visit a site they control, request a route supporting CORS, and then retrieve the token. With this token, they could possibly make requests to non CORS routes as this user.  A configuration and scenario where this would occur is unlikely, as most configurations will set CORS globally (where crumb is not used), or not at all.
<br><br>• Affected Versions: <3.0.0
<br>• Patched Versions: >=3.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/spumko/crumb/commit/5e6d4f5c81677fe9e362837ffd4a02394303db3c']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
