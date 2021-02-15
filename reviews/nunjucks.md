---
Publication-State: Active
Access: Public
Reviewers:
- Name: Matt Austin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/nunjucks
Review-Date: '2016-10-17'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in autoescape mode*<br><br>Upgrade to version 2.4.3 or later.
### Details
Nunjucks is a full featured templating engine for JavaScript.  Versions 2.4.2 and lower have a cross site scripting (XSS) vulnerability in autoescape mode.  In autoescape mode, all template vars should automatically be escaped.  By using an array for the keys, such as `name[]=<script>alert(1)</script>`, it is possible to bypass autoescaping and inject content into the DOM.
<br><br>• Affected Versions: <=2.4.2
<br>• Patched Versions: >=2.4.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/matt-/nunjucks_test', 'https://github.com/mozilla/nunjucks/issues/835']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
