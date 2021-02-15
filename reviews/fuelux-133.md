---
Publication-State: Active
Access: Public
Reviewers:
- Name: Keenan Jaenicke
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/fuelux
Review-Date: '2016-07-25'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in Pillbox*<br><br>Recommendation: Avoid the Pillbox functionality until a patch is available.
### Details
FuelUX is a library for extending Twitter Bootstrap with additional lightweight JavaScript controls.  There exists a cross site scripting (XSS) vulnerability in the Pillbox feature of FuelUX.  By supplying a script as a value for a new pillbox, it is possible to cause arbitrary script execution.    This advisory is being released before a public patched version is available because the issue was reported publicly on Github.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/ExactTarget/fuelux/issues/1841']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
