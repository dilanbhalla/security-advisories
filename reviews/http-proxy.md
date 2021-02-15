---
Publication-State: Active
Access: Public
Reviewers:
- Name: TJ Holowaychuk
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/http-proxy
Review-Date: '2017-04-11'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Insufficient Error Handling*<br><br>Upgrade to v0.7.0 or later.
### Details
Http-proxy is a proxying library.  Because of the way errors are handled in versions before 0.7.0, an attacker that forces an error can crash the server, causing a denial of service.
<br><br>• Affected Versions: <=0.6.6
<br>• Patched Versions: >=0.7.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/nodejitsu/node-http-proxy/pull/101)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
