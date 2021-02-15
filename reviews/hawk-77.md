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
- pkg:npm/hawk
Review-Date: '2016-01-19'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Update to hawk version 4.1.1 or greater.
### Details
Specifically crafted long headers or uris can cause a minor denial of service when using hawk versions less than 4.1.1.  "The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression to enter these extreme situations and then hang for a very long time."  Updates: - Updated to include fix in 3.1.3 
<br><br>• Affected Versions: < 3.1.3  || >= 4.0.0 <4.1.1
<br>• Patched Versions: >=3.1.3 < 4.0.0 || >=4.1.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/hueniverse/hawk/issues/168', 'https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
