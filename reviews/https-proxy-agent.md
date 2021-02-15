---
Publication-State: Active
Access: Public
Reviewers:
- Name: Kris Adler
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/https-proxy-agent
Review-Date: '2019-09-25'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Man-in-the-Middle*<br><br>Update https-proxy-agent module to version >=2.2.3
### Details
[https-proxy-agent] Socket returned without TLS upgrade on non-200 CONNECT response, allowing request data to be sent over unencrypted connection
<br><br>• Affected Versions: <2.2.3
<br>• Patched Versions: >=2.2.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/541502']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
