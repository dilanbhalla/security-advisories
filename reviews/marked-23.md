---
Publication-State: Active
Access: Public
Reviewers:
- Name: Barış Soner Uşaklı
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/marked
Review-Date: '2015-01-22'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Recommendation: Update to marked v0.3.4 or later.
### Details
Marked 0.3.3 and earlier is vulnerable to regular expression denial of service (ReDoS) when certain types of input are passed in to be parsed.  "The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression to enter these extreme situations and then hang for a very long time." [1]  Marked's catastrophic backtracking issue for the `em` inline rule has now been patched in 0.3.4.
<br><br>• Affected Versions: <=0.3.3
<br>• Patched Versions: >=0.3.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS', 'https://github.com/chjj/marked/issues/497']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
