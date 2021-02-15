---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jordan Harband
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/forms
Review-Date: '2017-04-11'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Lack of HTML Escaping*<br><br>Recommendation: Upgrade to version 1.3.0 or later
### Details
Forms is a library for easily creating HTML forms. Versions before 1.3.0 did not have proper html escaping.  This means that if the application did not sanitize html on behalf of forms, use of forms may be vulnerable to cross site scripting
<br><br>• Affected Versions: <1.3.0
<br>• Patched Versions: >=1.3.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/caolan/forms/commit/bc01e534a0ff863dedb2026a50bd03153bbc6a5d']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
