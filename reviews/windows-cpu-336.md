---
Publication-State: Active
Access: Public
Reviewers:
- Name: Daniel Bond
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/windows-cpu
Review-Date: '2017-05-19'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Command Execution*<br><br>Recommendation: Avoid passing user input to the findLoad method. If you must, pass user input through a sanitizer (such as a shell escaping tool) prior to passing it to findLoad.
### Details
Windows-cpu is a CPU monitoring utility for windows.  The findLoad method passes a provided string directly to the shell, allowing arbitrary command execution.   Proof of Concept: This code will open the built-in calculator program. ``` var win = require('windows-cpu'); wind.findLoad('foo & calc.exe'); ```
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <=0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/KyleRoss/windows-cpu/blob/master/index.js#L81']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
