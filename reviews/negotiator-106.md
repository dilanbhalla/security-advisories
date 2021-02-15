---
Publication-State: Active
Access: Public
Reviewers:
- Name: Adam Baldwin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/negotiator
Review-Date: '2016-06-16'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Recommendation: Upgrade to at least version 0.6.1  Express users should update to Express 4.14.0 or greater. If you want to see if you are using a vulnerable call,  a quick grep for the `acceptsLanguages` function call in your application will tell you if you are using this functionality.
### Details
negotiator is an HTTP content negotiator for Node.js and is used by many modules and frameworks including Express and Koa.  The header for "Accept-Language", when parsed by negotiator is vulnerable to Regular Expression Denial of Service via a specially crafted string.   Timeline  - April 29th 2016 - Initial report to maintainers - April 29th 2016 - Confirm receipt from maintainers - May 1st 2016 - Fix confirmed - May 5th 2016 - 0.6.1 published with fix - June 16th 2016 - Advisory published (delay was to coordinate fixes in upstream frameworks, Koa and Express)
<br><br>• Affected Versions: <= 0.6.0
<br>• Patched Versions: >= 0.6.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
