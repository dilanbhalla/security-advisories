---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jim O'Brien
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/sanitize-html
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross Site Scripting*<br><br>Upgrade to version 1.2.3 or later.
### Details
sanitize-html is a library for scrubbing html input for malicious values Versions 1.2.2 and below have a cross site scripting vulnerability under certain scenarios:  Entering the following:  `<IMG SRC= onmouseover="alert('XSS');">` produces the following:  `<img src="onmouseover="alert('XSS');"" />` This is definitely invalid HTML, but would suggest that it's being interpreted incorrectly by the parser.
<br><br>• Affected Versions: <=1.2.2
<br>• Patched Versions: >=1.2.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/punkave/sanitize-html/issues/19', 'https://github.com/punkave/sanitize-html/pull/20']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
