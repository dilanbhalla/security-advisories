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
Review-Date: '2015-12-28'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Route level CORS config overrides connection level defaults*<br><br>You should install hapi v11.1.4 or newer if you combine server level, connection level, or route level CORS configuration.
### Details
When server level, connection level or route level CORS configurations are combined and when a higher level config included security restrictions (like origin), a higher level config that included security restrictions (like origin) would have those restrictions overridden by less restrictive defaults (e.g. origin defaults to all origins `*`).
<br><br>• Affected Versions: <11.1.4
<br>• Patched Versions: >=11.1.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/hapijs/hapi/issues/2980']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
