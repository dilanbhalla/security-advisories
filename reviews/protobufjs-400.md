---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jamie Davis
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/protobufjs
Review-Date: '2018-03-31'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of Service*<br><br>Recommendation: update protobufjs to 6.8.6 or higher
### Details
`protobufjs` is vulnerable to ReDoS when parsing crafted invalid *.proto files
<br><br>• Affected Versions: <=6.8.5
<br>• Patched Versions: >=5.0.3 <6.0.0 || >=6.8.6
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/319576', 'https://github.com/dcodeIO/protobuf.js/blob/6.8.5/src/parse.js#L27']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
