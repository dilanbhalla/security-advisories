---
Publication-State: Active
Access: Public
Reviewers:
- Name: Ivan Kozik
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/serve-index
Review-Date: '2015-03-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-Site Scripting*<br><br>* Update to version 1.6.3 or greater
### Details
When using serve-index middleware version < 1.6.3 file and directory names are not escaped in HTML output. If remote users can influence file or directory names, this can trigger a persistent XSS attack.
<br><br>• Affected Versions: <1.6.3
<br>• Patched Versions: >=1.6.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/expressjs/serve-index/issues/28', 'https://www.owasp.org/index.php/Cross-site_Scripting_%28XSS%29']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
