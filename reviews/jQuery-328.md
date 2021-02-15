---
Publication-State: Active
Access: Public
Reviewers:
- Name: Egor Homakov
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/jQuery
Review-Date: '2017-03-21'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-Site Scripting (XSS)*<br><br>Upgrade to v3.0.0 or greater.
### Details
Jquery is a javascript library for DOM traversal and manipulation, event handling, animation, and Ajax.   When text/javascript responses are received from cross-origin ajax requests not containing the option `dataType`, the result is executed in `jQuery.globalEval` potentially allowing an attacker to execute arbitrary code on the origin.
<br><br>• Affected Versions: >=1.4.0 <=1.11.3 || >=1.12.3 <=2.2.4
<br>• Patched Versions: >=3.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/jquery/jquery/issues/2432)', 'https://github.com/jquery/jquery/commit/b078a62013782c7424a4a61a240c23c4c0b42614)', 'https://github.com/jquery/jquery/pull/2588)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
