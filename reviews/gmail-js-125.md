---
Publication-State: Active
Access: Public
Reviewers:
- Name: Gursev Singh Kalra
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/gmail-js
Review-Date: '2016-07-21'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*DOM-based XSS*<br><br>Recommendation: Since there is no public patch yet available, it may be best to avoid using these functions altogether for the time being.
### Details
gmail-js is a client side library for interacting with the Gmail API.  Three functions exposed by the Gmail.js API (not the Google Gmail API) are vulnerable to [DOM-based cross site scripting](https://www.owasp.org/index.php/DOM_Based_XSS) (DOMXSS).  The three functions are `tools.parse_response`, `helper.get.visible_emails_post`, and `helper.get.email_data_post`.  Each one of these functions calls `new Function()` with user data passed as the argument.  This vulnerability is being disclosed before a public patched version is available because the issue was reported in a public Github issue.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/KartikTalwar/gmail.js/issues/281', 'https://www.owasp.org/index.php/DOM_Based_XSS']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
