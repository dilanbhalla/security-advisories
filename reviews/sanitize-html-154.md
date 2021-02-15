---
Publication-State: Active
Access: Public
Reviewers:
- Name: Andrew Krasichkov
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/sanitize-html
Review-Date: '2017-04-11'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross Site Scripting*<br><br>Recommendation: Upgrade to version 1.11.4 or later
### Details
Sanitize-html is a library for scrubbing html input of malicious values.  Versions 1.11.1 and below are vulnerable to cross site scripting (XSS) in certain scenarios:  If allowed at least one nonTextTags, the result is a potential XSS vulnerability. PoC:  ``` var sanitizeHtml = require('sanitize-html');  var dirty = '!<textarea>&lt;/textarea&gt;<svg/onload=prompt`xs`&gt;</textarea>!'; var clean = sanitizeHtml(dirty, {     allowedTags: [ 'textarea' ] });  console.log(clean);  // !<textarea></textarea><svg/onload=prompt`xs`></textarea>! ```
<br><br>• Affected Versions: <=1.11.1
<br>• Patched Versions: >=1.11.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/punkave/sanitize-html/issues/100', 'https://github.com/punkave/sanitize-html/commit/5d205a1005ba0df80e21d8c64a15bb3accdb2403']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
