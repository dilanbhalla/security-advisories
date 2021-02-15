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
- pkg:npm/superstatic
Review-Date: '2018-04-29'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Path Traversal*<br><br>Update to version 5.0.2 or higher.
### Details
`superstatic` is vulnerable to path traversal on Windows. Additionally, it is vulnerable to path traversal on other platforms combined with certain Node.js versions which erroneously normalize `\` to `/` in paths on all platforms (a known example being Node.js v9.9.0).
<br><br>• Affected Versions: <=5.0.1
<br>• Patched Versions: >=5.0.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/319951', 'https://github.com/firebase/superstatic/blob/v5.0.1/lib/providers/fs.js#L71', 'https://github.com/firebase/superstatic/commit/e396ff62f588732989137d6c40d46b310e51ef2b', 'https://github.com/firebase/superstatic/pull/255', 'https://github.com/firebase/superstatic/releases/tag/v5.0.2']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
