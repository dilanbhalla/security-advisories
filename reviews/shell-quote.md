---
Publication-State: Active
Access: Public
Reviewers:
- Name: Koki Takahashi, Node Security Team
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/shell-quote
Review-Date: '2016-06-21'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Potential Command Injection*<br><br>Upgrade to at least version 1.6.1
### Details
The npm module "shell-quote" cannot correctly escape ">" and "<" operator used for redirection in shell. I'm wondering if this might be possible vulnerability for many application which depends on shell-quote.  For example:     const quote = require('shell-quote').quote;    console.log(quote(['foo>bar']));  will print "foo>bar", where "foo\>bar" is desirable.  This module is downloaded more than 1M times per month and many other modules are depending on this. If an application is escaping command-line args with this module, they might be vulnerable from malicious user input.  For example: ``` var sq = require('../tests/get/shell-quote-1.6.0'); var exec = require('child_process').exec;  var pattern = process.argv[2];  command = sq.quote(['grep', pattern])); exec('cat file | ' + command, function ( err, stdout, stderr) {     console.log(command, stdout);    }); ``` will be vulnerable when user input something like pattern = ':</etc/passwd', which causes the content of /etc/passwd to be leaked.  Internally, (Jon Lamendola, Nick Starke, Jacob Waddell) found that the `;`, `{`, and `}` characters weren't escaped properly either. This allows for full command injection. A malicious user could input `'a;{echo,test,123,234}'` to execute echo fully.
<br><br>• Affected Versions: <=1.6.0
<br>• Patched Versions: >=1.6.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
