---
Publication-State: Active
Access: Public
Reviewers:
- Name: Peter Dotchev
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/uri-js
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial Of Service*<br><br>Recommendation: Upgrade to v3.0.0
### Details
uri-js is a module that tries to fully implement RFC 3986. One of these features is validating whether or not a supplied URL is valid or not. To do this, uri-js uses a regular expression, This regular expression is vulnerable to redos. This causes the program to hang and the CPU to idle at 100% usage while uri-js is trying to validate if the supplied URL is valid or not.  To check if you're vulnerable, look for a call to `require("uri-js").parse()` where a user is able to send their own input.
<br><br>• Affected Versions: <=2.1.1
<br>• Patched Versions: >=3.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/garycourt/uri-js/issues/12', 'https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
