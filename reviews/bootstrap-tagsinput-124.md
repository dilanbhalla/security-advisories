---
Publication-State: Active
Access: Public
Reviewers:
- Name: Alex Wong
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/bootstrap-tagsinput
Review-Date: '2016-07-20'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in itemTitle parameter*<br><br>Recommendation: Avoid using the `itemTitle` parameter until a patch is available
### Details
Bootstrap Tags Input is a jQuery plugin providing a Twitter Bootstrap user interface for managing tags.   Version 0.8.0 contains a cross site scripting vulnerability (XSS) via the `itemTitle` parameter. By supplying a malicious value for this parameter, it is possible to execute arbitrary code.  This vulnerability is being disclosed before a public patched release is available because of an existing Github issue which is already public.
<br><br>• Affected Versions: <=0.8.0
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/bootstrap-tagsinput/bootstrap-tagsinput/issues/501']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
