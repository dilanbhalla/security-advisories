---
Publication-State: Active
Access: Public
Reviewers:
- Name: Brendan Scarvell of Console
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/gm
Review-Date: '2015-10-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Command Injection in gm.compare function*<br><br>Update to version 1.21.1 or greater.
### Details
gm version 1.20.0 and below are vulnerable to command injection when user input is passed into the arguments of the `gm.compare `function. The `compare()` function fails to sanitize meta characters correctly before calling the graphics magic binary.
<br><br>• Affected Versions: <=1.20.0
<br>• Patched Versions: >=1.21.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/aheckmann/gm/commit/5f5c77490aa84ed313405c88905eb4566135be31']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
