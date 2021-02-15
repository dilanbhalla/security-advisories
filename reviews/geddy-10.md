---
Publication-State: Active
Access: Public
Reviewers:
- Name: Vikram Chaitanya
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/geddy
Review-Date: '2015-07-27'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>Recommendation: Update to version >= 13.0.8
### Details
Geddy static file serving allows directory traversal with a URI encoded path.  ### Example ``` http://localhost:4000/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd  geddy is serving the output as it doesn't match the routes and it's a static file ```
<br><br>• Affected Versions: <13.0.8
<br>• Patched Versions: >=13.0.8
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/geddy/geddy/issues/697', 'https://github.com/geddy/geddy/pull/699']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
