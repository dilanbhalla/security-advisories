---
Publication-State: Active
Access: Public
Reviewers:
- Name: Gabrielle Bourdages
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/ag-grid
Review-Date: '2017-03-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS via Angular Expression*<br><br>Avoid using ag-grid in combination with AngularJS until a fix is available.
### Details
ag-grid is an advanced data grid that is library agnostic.  ag-grid is vulnerable to Cross-site Scripting (XSS) via Angular Expressions, if AngularJS is used in combination with ag-grid.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/ceolter/ag-grid/issues/1287', 'https://spring.io/blog/2016/01/28/angularjs-escaping-the-expression-sandbox-for-xss']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
