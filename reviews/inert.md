---
Publication-State: Active
Access: Public
Reviewers:
- Name: Gil Pedersen
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/inert
Review-Date: '2014-12-16'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Hidden Directories Always Served*<br><br>Update to version >= 1.1.1.
### Details
The inert directory handler always allows files in hidden directories to be served, even when `showHidden` is false.
<br><br>• Affected Versions: <1.1.1
<br>• Patched Versions: >=1.1.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/hapijs/inert/pull/15', 'https://github.com/hapijs/inert/commit/e8f99f94da4cb08e8032eda984761c3f111e3e82']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
