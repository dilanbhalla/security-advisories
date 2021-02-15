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
- pkg:npm/marked
Review-Date: '2014-01-31'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Multiple Content Injection Vulnerabilities*<br><br>- Upgrade to version 0.3.1 or later
### Details
Marked comes with an option to sanitize user output to help protect against content injection attacks.  ```sanitize: true```  Even if this option is set, marked is vulnerable to content injection in multiple locations if untrusted user input is allowed to be provided into marked and that output is passed to the browser.  Injection is possible in two locations  - gfm codeblocks (language) - javascript url's
<br><br>• Affected Versions: <=0.3.0
<br>• Patched Versions: >=0.3.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
