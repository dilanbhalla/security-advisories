---
Publication-State: Active
Access: Public
Reviewers:
- Name: James Halliday
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/ecstatic
Review-Date: '2015-12-23'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of Service - Illegal access crash from if-modified-since header*<br><br>Upgrade to ecstatic version 1.4.0 or greater.
### Details
Certain input strings when passed to new Date() or Date.parse() will cause v8 to raise an exception. This leads to a crash and denial of service in ecstatic  when this input is passed into the server via the If-Modified-Since header.
<br><br>• Affected Versions: <1.4.0
<br>• Patched Versions: >=1.4.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/jfhbrook/node-ecstatic/pull/179', 'https://bugs.chromium.org/p/v8/issues/detail?id=4640']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
