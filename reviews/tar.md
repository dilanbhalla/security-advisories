---
Publication-State: Active
Access: Public
Reviewers:
- Name: Tim Cuthbertson
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/tar
Review-Date: '2015-11-03'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Symlink Arbitrary File Overwrite*<br><br>Update to a version 2.0.0 or greater
### Details
The `tar` module earlier than version 2.0.0 allow for archives to contain symbolic links that will overwrite targets outside the expected path for extraction.
<br><br>• Affected Versions: <2.0.0
<br>• Patched Versions: >=2.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/npm/npm/releases/tag/v2.7.5']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
