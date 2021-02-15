---
Publication-State: Active
Access: Public
Reviewers:
- Name: Todd Wolfson
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/pivottable
Review-Date: '2016-08-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-Site Scripting (XSS)*<br><br>Recommendation: Upgrade to version 2.0.0 or later.
### Details
PivotTable.js is a Javascript Pivot Table library with drag'n'drop functionality built on top of jQuery/jQueryUI.  Due to a change from text to html functions in how JSON elements are rendered, a cross site scripting (XSS) vulnerability was introduced in version 1.4.0.  This vulnerability remained in place until version 2.0.0.
<br><br>• Affected Versions: >=1.4.0 <2.0.0
<br>• Patched Versions: >=2.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/nicolaskruchten/pivottable/pull/401']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
