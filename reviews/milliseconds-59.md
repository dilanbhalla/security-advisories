---
Publication-State: Active
Access: Public
Reviewers:
- Name: Luigi Pinca
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/milliseconds
Review-Date: '2015-11-20'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Update to version 0.1.2 or greater. An alternative would be to limit the input length of the user input before passing it into millisecond to under 10k characters.
### Details
millisecond is vulnerable to regular expression denial of service (ReDoS) when extremely long version strings are parsed.  "The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression to enter these extreme situations and then hang for a very long time."[1]  ## Proof of concept ``` var ms = require('millisecond'); var genstr = function (len, chr) {    var result = "";    for (i=0; i<=len; i++) {        result = result + chr;    }     return result; }  ms(genstr(process.argv[2], "5") + " minutea"); ```
<br><br>• Affected Versions: <0.1.2
<br>• Patched Versions: >=0.1.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS', 'https://github.com/unshiftio/millisecond/pull/4']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
