---
Publication-State: Active
Access: Public
Reviewers:
- Name: Liang Gong
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/windows-build-tools
Review-Date: '2017-01-06'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Downloads Resources over HTTP*<br><br>Recommendation: Update to version 1.0.0 or later
### Details
windows-build-tools is a module for installing C++ Build Tools for Windows using npm.  windows-build-tools versions below 1.0.0 download resources over HTTP, which leaves it vulnerable to MITM attacks. It may be possible to cause remote code execution (RCE) by swapping out the requested resources with an attacker controlled copy if the attacker is on the network or positioned in between the user and the remote server.
<br><br>• Affected Versions: <1.0.0
<br>• Patched Versions: >=1.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/felixrieseberg/windows-build-tools/commit/9835d33e68f2cb5e4d148e954bb3ed0221d98e90']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
