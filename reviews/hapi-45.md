---
Publication-State: Active
Access: Public
Reviewers:
- Name: Eran Hammer
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/hapi
Review-Date: '2015-10-20'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Incorrect handling of CORS preflight request headers*<br><br>Updated to hapi version 11.0.0 or greater
### Details
Hapi versions less than 11.0.0 implement CORS incorrectly and allowed for configurations that at best returned inconsistent headers and at worst allowed cross-origin activities that were expected to be forbidden. [1]  'If the connection has CORS enabled but one route has it off, and the route is not GET, the OPTIONS prefetch request will return the default CORS headers and then the actual request will go through and return no CORS headers. This defeats the purpose of turning CORS on the route.' [2]
<br><br>• Affected Versions: <11.0.0
<br>• Patched Versions: >=11.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/hapijs/hapi/issues/2850', 'https://github.com/hapijs/hapi/issues/2840']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
