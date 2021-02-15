---
Publication-State: Active
Access: Public
Reviewers:
- Name: JelteF
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/Morris.js
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in Hover Over Label Names*<br><br>Recommendation: Escape the label names. They can be escaped using only a few lines of code. A pull request with a fix has been merged on GitHub, but not published to npm. This can be found on [Github.](https://github.com/morrisjs/morris.js/commit/1c66cfc4ac7b23d324f131bec7739265887e30fc)
### Details
Morris.js creates an svg graph, with labels that appear when hovering over a point. The hovering label names are not escaped. If control over the labels is obtained, script can be injected. The script will run on the client side whenever that specific graph is loaded.
<br><br>• Affected Versions: <=0.5.0
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/morrisjs/morris.js/pull/464']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
