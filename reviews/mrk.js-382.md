---
Publication-State: Active
Access: Public
Reviewers:
- Name: joker314
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/mrk.js
Review-Date: '2018-03-03'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in links*<br><br>Recommendation: update mrk.js to version 2.0.1 and use mark.sanitizeURL() for any attributes when extending the md
### Details
mrk.js suffered from a XSS vulnerability when markdown was converted to HTML.
<br><br>• Affected Versions: <2.0.1
<br>• Patched Versions: >=2.0.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/heyitsmeuralex/mrk/pull/3']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
