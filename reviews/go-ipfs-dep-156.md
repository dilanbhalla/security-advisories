---
Publication-State: Active
Access: Public
Reviewers:
- Name: Scott Hardy & Adam Baldwin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/go-ipfs-dep
Review-Date: '2016-12-16'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Downloads Resources over HTTP*<br><br>Update to version 0.4.4 or greater
### Details
During the installation process, the go-ipfs-deps module insecurely downloads resources over HTTP. This allows for a MITM attack to compromise the integrity of the resources used by this module and could allow for further compromise.
<br><br>• Affected Versions: <0.4.4
<br>• Patched Versions: >=0.4.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/diasdavid/go-ipfs-dep/pull/12']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
