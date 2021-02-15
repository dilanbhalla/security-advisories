---
Publication-State: Active
Access: Public
Reviewers:
- Name: Xiao Long
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/marked
Review-Date: '2015-01-22'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*VBScript Content Injection*<br><br>Recommendation: Update to version 0.3.3 or greater.
### Details
Marked 0.3.2 and earlier is vulnerable to content injection even when `sanitize: true` is enabled.  `[xss link](vbscript:alert(1&#41;)`  will get a link  `<a href="vbscript:alert(1)">xss link</a>`  this script does not work in IE 11 edge mode, but works in IE 10 compatibility view.
<br><br>• Affected Versions: <=0.3.2
<br>• Patched Versions: >=0.3.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/chjj/marked/issues/492']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
