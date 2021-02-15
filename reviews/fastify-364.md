---
Publication-State: Active
Access: Public
Reviewers:
- Name: nwoltman
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/fastify
Review-Date: '2018-01-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Fastify denial-of-service vulnerability with large JSON payloads*<br><br>Update to version 0.38.0 or later.
### Details
Fastify prior to 0.37.0 is vulnerable to a denial-of-service attack by sending a request with Content-Type set to application/json and a very large payload.
<br><br>• Affected Versions: <=0.37.0
<br>• Patched Versions: >=0.38.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/fastify/fastify/commit/fabd2a011f2ffbb877394abe699f549513ffbd76', 'https://github.com/fastify/fastify/releases/tag/v0.38.0', 'https://hackerone.com/reports/303632']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
