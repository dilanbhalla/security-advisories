---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jon Merrifield
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/rendr
Review-Date: '2016-07-25'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in client rendered block templates*<br><br>Recommendation: Upgrade to rendr version 1.1.4
### Details
Rendr-handlebars is a library that allows the handlebars templating engine to be used with Rendr framework projects.  The templating can occur either on the client or the server.  Versions up to 1.1.3 have a cross site scripting (XSS) issue when rendered inside a `_block` during client side rendering. Server side rendering is not affected and is properly escaped.
<br><br>• Affected Versions: <=1.1.3
<br>• Patched Versions: >=1.1.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/rendrjs/rendr-handlebars/pull/61', 'https://github.com/rendrjs/rendr/pull/513']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
