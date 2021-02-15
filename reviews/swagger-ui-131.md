---
Publication-State: Active
Access: Public
Reviewers:
- Name: Joe Vennix
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/swagger-ui
Review-Date: '2016-07-25'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS via Content-type header*<br><br>Recommendation: Update to 2.1.5 or later.
### Details
By using a malicious server which returns script as the value of the Content-Type header, it is possible to execute arbitrary code using the demonstration capabilities of Swagger-UI.
<br><br>• Affected Versions: 2.1.4
<br>• Patched Versions: >=2.1.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/swagger-api/swagger-ui/issues/1863']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
