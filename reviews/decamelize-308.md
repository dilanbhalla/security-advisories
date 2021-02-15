---
Publication-State: Active
Access: Public
Reviewers:
- Name: saurik
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/decamelize
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Recommendation: Upgrade to version 1.1.2 or later.
### Details
Decamelize is used to convert a dash/dot/underscore/space separated string to camelCase.   Decamelize uses regular expressions to evaluate a string and takes unescaped separator values, which can be used to create a denial of service attack.
<br><br>• Affected Versions: >=1.1.0 <=1.1.1
<br>• Patched Versions: >=1.1.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/sindresorhus/decamelize/issues/5']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
