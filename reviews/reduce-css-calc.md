---
Publication-State: Active
Access: Public
Reviewers:
- Name: Сковорода Никита Андреевич
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/reduce-css-calc
Review-Date: '2016-10-17'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Arbitrary Code Injection*<br><br>Update to version 1.2.5 or later
### Details
Arbitrary code execution is possible through crafted css.  This makes cross sites scripting (XSS) possible on the client and arbitrary code injection possible on the server and user input is passed to the `calc` function.
<br><br>• Affected Versions: <=1.2.4
<br>• Patched Versions: >=1.2.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://gist.github.com/ChALkeR/415a41b561ebea9b341efbb40b802fc9']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
