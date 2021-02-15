---
Publication-State: Active
Access: Public
Reviewers:
- Name: Andrea Giammarchi
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/emojione
Review-Date: '2016-07-25'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in primary functions*<br><br>Recommendation: Upgrade to version 1.3.1 or latest.
### Details
Emojione is a module built to facilitate translating between emoji and shortcodes.  Version 1.3.0 and below have four primary functions:  * toShort() * shortnameToImage() * unicodeToImage() * toImage()  All four do not properly sanitize input and are thus vulnerable to cross site scripting (XSS).  If you application passes user supplied input to these functions, it may be vulnerable to this attack.
<br><br>• Affected Versions: <=1.3.0
<br>• Patched Versions: >=1.3.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/Ranks/emojione/issues/61']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
