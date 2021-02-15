---
Publication-State: Active
Access: Public
Reviewers:
- Name: Ilya Kantor
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/send
Review-Date: '2014-09-12'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>Upgrade to a version greater than or equal to 0.8.4.
### Details
When relying on the root option to restrict file access it may be possible for an application consumer to escape out of the restricted directory and access files in a similarly named directory. For example, `static(_dirname + '/public')` would allow access to `_dirname + '/public-restricted'`.
<br><br>• Affected Versions: < 0.8.4
<br>• Patched Versions: >= 0.8.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/visionmedia/send/pull/59', 'https://github.com/visionmedia/send/commit/9c6ca9b2c0b880afd3ff91ce0d211213c5fa5f9a']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
