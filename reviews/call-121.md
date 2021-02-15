---
Publication-State: Active
Access: Public
Reviewers:
- Name: Nicolas Morel
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/call
Review-Date: '2016-07-05'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Invalid input to route validation rules*<br><br>Upgrade to call 3.0.2.  hapi users should upgrade to 13.4.2.
### Details
call is an HTTP router that is primarily used by the hapi framework.  There exists a bug in call versions 2.0.1-3.0.1 that does not validate empty parameters, which could result in invalid input bypassing the route validation rules.  For example, in the routing scheme `/api/{param}/{param2}/details`, a request made to `/api///` would match incorrectly.
<br><br>• Affected Versions: >= 2.0.1 <3.0.2
<br>• Patched Versions: >=3.0.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/hapijs/hapi/issues/3228']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
