---
Publication-State: Active
Access: Public
Reviewers:
- Name: Aleksandr Dobkin and Sebastian Roschke
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/yui
Review-Date: '2017-03-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS via .swf files*<br><br>YUI has published their recommendation to fix this issue.  Their recommendation is to:  - Delete self-hosted copies of these files if you are not using them  - Use the Yahoo! CDN hosted files  - Use the patched files provided on the YUI Library [here](https://yuilibrary.com/support/20130515-vulnerability/#resolution).
### Details
YUI is a free, open source JavaScript and CSS framework for building richly interactive web applications.  In the vulnerable versions, the `uploader.swf` and `io.swf` utilities contain a vulnerability allowing cross-site scripting through the `.swf` files used in these components. Through a url accessing these files, and attacker can inject script in the context of these files, potentially exposing cookies or other sensitive information.  The vulnerability resurfaced in v0.10.2, but only with `io.swf`.
<br><br>• Affected Versions: >=3.0.0 <=3.9.1 || =3.10.2
<br>• Patched Versions: =3.10.1 || >=3.10.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://yuilibrary.com/support/20130515-vulnerability/)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
