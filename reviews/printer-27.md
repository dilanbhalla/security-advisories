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
- pkg:npm/printer
Review-Date: '2014-03-06'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Potential Command Injection*<br><br>- Update to version > 0.0.1 which is available on github at https://github.com/tojocky/node-printer
### Details
printer does not sanitize command arguments properly in the ```printDirect()``` function. If untrusted client input is passed in, command injection is possible.  Special thanks to [Wes Cruver](https://github.com/chieffancypants) for providing a pull request!
<br><br>• Affected Versions: <= 0.0.1
<br>• Patched Versions: > 0.0.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/tojocky/node-printer', 'https://github.com/tojocky/node-printer/commit/e001e38738c17219a1d9dd8c31f7d82b9c0013c7']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
